import streamlit as st
from typing import TypedDict
from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage
from prompt_store import get_prompt
from create_llm_message import create_llm_msg
from clarify_agent import ClarifyAgent
from smalltalk_agent import SmallTalkAgent
from policy_agent import PolicyAgent
from quota_agent import QuotaAgent
from segmentation_agent import SegmentationAgent
from STARDT_agent import StardtAgent

class AgentState(TypedDict):
    message_history: list[BaseMessage]
    lnode: str
    incremental_response: str
    category: str
    initial_message: str

class Category(BaseModel):
    category: str

VALID_CATEGORIES = ["classifier", "smalltalk", "clarify", "policy", "quota", "segmentation", "stardt"]

class SalesOpsAgent:
    def __init__(self, api_key):
        self.model = ChatOpenAI(model=st.secrets['OPENAI_MODEL'], api_key=api_key)

        self.smalltalk_agent_class = SmallTalkAgent(self.model)
        self.clarify_agent_class = ClarifyAgent(self.model)
        self.policy_agent_class = PolicyAgent(self.model)
        self.quota_agent_class = QuotaAgent(self.model)
        self.segmentation_agent_class = SegmentationAgent(self.model)
        self.stardt_agent_class = StardtAgent(self.model)

        workflow = StateGraph(AgentState)
        workflow.add_node("classifier", self.initial_classifier)
        workflow.add_node("smalltalk", self.smalltalk_agent_class.smalltalk_agent)
        workflow.add_node("clarify", self.clarify_agent_class.clarify_agent)
        workflow.add_node("policy", self.policy_agent_class.policy_agent)
        workflow.add_node("quota", self.quota_agent_class.quota_agent)
        workflow.add_node("segementation", self.segmentation_agent_class.segmentation_agent)
        workflow.add_node("stardt", self.stardt_agent_class.stardt_agent)

        workflow.add_conditional_edges("classifier", self.main_router)
        workflow.add_edge(START, "classifier")
        workflow.add_edge("smalltalk", END)
        workflow.add_edge("clarify", END)
        workflow.add_edge("policy", END)
        workflow.add_edge("quota", END)
        workflow.add_edge("segmentation", END)
        workflow.add_edge("stardt", END)

        self.graph = workflow.compile()

    def initial_classifier(self, state: AgentState):
        print("initial classifier")
        classifier_prompt = get_prompt("classifier")
        llm_messages = create_llm_msg(classifier_prompt, state['message_history'])
        llm_response = self.model.with_structured_output(Category).invoke(llm_messages)
        category = llm_response.category
        print(f"category is {category}")
        return {
            "lnode": "initial_classifier",
            "category": category,
        }
    
    def main_router(self, state: AgentState):
        my_category = state['category']
        if my_category in VALID_CATEGORIES:
            return my_category
        else:
            print(f"unknown category: {my_category}")
            return END