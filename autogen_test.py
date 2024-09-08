import autogen

config_list = [
    {
        'model':'gpt-4',
        'api_key': ''
    }
]

llm_config={
    #"request_timeout": 600, 
    "seed": 42, 
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant", 
    llm_config=llm_config,
    system_message= "My First Assistant"
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy", 
    human_input_mode = "TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content","").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir":"out"},
    llm_config=llm_config,
    system_message="""reply terminate if solved, else reply continue"""
)

task = """
Write python code to give add numbers 1 through 10 and store the code in a file called sum.py
"""
user_proxy.initiate_chat(
    assistant,
    message=task
)





