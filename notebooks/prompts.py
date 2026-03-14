ORACLE_GEN_PROMPT = """
    You are generating training data for Retrieval-Augmented Fine-Tuning (RAFT).

    Given the document chunk below, generate EXACTLY 10 independent, high-quality, non-trivial and diverse training examples.

    For each example:

    1. Generate a question  that can ONLY be answered from this chunk .
    2. Extract the minimal span of text necessary to answer it (oracle_context).
    3. Provide a detailed chain-of-thought answer grounded ONLY in oracle_context.

    Strict Rules:
    - Do NOT use any outside knowledge that is not present in the chunk given.
    - Oracle context must be copied verbatim from the chunk (no paraphrasing).
    - CoT answer must reason step-by-step using oracle_context.
    - CoT reasoning must reference oracle_context explicitly
    - Each question must target a different part of the chunk.
    - If the chunk is insufficient for 10 good questions, generate the best possible non-overlapping ones.

    OUTPUT INSTRUCTIONS:
    - Generate exactly 10 samples.
    - Return ONLY the JSON List. 
    - Do not include any conversational filler (e.g., "Here is your JSON...").

    Document chunk:
    {chunk}
    """


RAFT_COT_GEN_PROMPT = """
    You are a RAFT (Retrieval Augmented Fine-Tuning) data generator.
    Your goal is to create a training sample where a model learns to ignore 'distractor' noise and find the 'oracle' truth to answer the question asked.

    <ORACLE_CONTEXT>:
    {oracle_context}

    <DISTRACTOR_CONTEXTS>:
    {distractor_contexts}

    <QUESTION>:
    {question}

    TASK:
    1. Generate a "Chain-of-Thought" (CoT) reasoning steps that lead to the answer.
    2. The reasoning must explicitly cite the information from the Oracle Context.
    3. In the reasoning, if you need to copy paste some sentences 
                from the context, include them in ##begin_quote## and ##end_quote##. 
                This would mean that things outside of ##begin_quote## and 
                ##end_quote## are not directly copy paste from the context.
    4. Provide the final concise answer.

    """



RFT_EVAL_DATA_GEN = """
    As an assistant, you need to first assess the complexity of the problem and adopt an appropriate thinking framework before providing the final solution. 
    Structure your response into two main sections: 

    Thought and Solution.\n
    First evaluate the complexity of the problem, then choose a suitable thinking framework, and describe the thought process as detailed as possible:\n
    1. For simple problems:\n
    **Analysis:**\n[Understand the core elements and goals of the problem]\n
    **Approach:**\n[Propose direct solution methods]\n
    **Summary:**\n[Concisely summarize the solution approach and key points]\n2. For moderately complex problems:\n
    **Analysis:**\n[Understand the problem and identify key points and challenges]\n
    **Initial Approach:**\n[Propose preliminary solutions]\n
    **Reflection:**\n[Evaluate the pros and cons of the initial approach]\n
    **Improvement:**\n[Refine the solution based on reflection]\n
    **Summary:**\n[Summarize the key points of the final solution]\n3. 

    For highly complex problems:\n
    **Analysis:**\n[Analyze various aspects of the problem and break down its structure]\n
    **Problem Decomposition:**\n[Break complex problem into manageable sub-problems]\n
    **Sub-problem Processing:** (Repeat the following steps for each sub-problem)\n
    - Sub-problem 1:\n  * Initial approach\n  * Reflection\n  * Improved solution\n- Sub-problem 2:\n  * Initial approach\n  * Reflection\n  * Improved solution\n- ...(adjust according to the actual number of sub-problems)\n
    **Integration:**\n[Integrate sub-problem solutions into a complete solution]\n
    **Overall Reflection:**\n[Evaluate the integrated complete solution]\n
    **Final Optimization:**\n[Make final optimizations based on overall reflection]\n
    **Summary:**\n[Summarize key points of the final comprehensive solution]\nThe solution section should maintain logical, accurate, and concise expression, detailing the steps needed to reach the conclusion, formatted as:\n

    **Solution:**\n[Provide the final solution here]

    Problem:
    {problem}

"""


RFT_EVAL_DATA_GEN_CONCISE = """

    You are a mathematical reasoning assistant. Your goal is to solve the provided problem by first thinking deeply and then providing a concise, step-by-step solution.

    Structure your response into two main sections: <think> and <answer>. Respond ONLY using the tags <think> and <answer>.

    <think>
        Assess the complexity of the problem and follow the corresponding framework:

        **If the problem is Simple:**
        - **Analysis:** [Core elements and goals]
        - **Approach:** [Direct solution methods]
        - **Summary:** [Concisely summarize key points]

        **If the problem is Moderately Complex:**
        - **Analysis:** [Key points and challenges]
        - **Initial Approach:** [Preliminary solutions]
        - **Reflection:** [Evaluate pros/cons]
        - **Improvement:** [Refine the solution]
        - **Summary:** [Final solution key points]

        **If the problem is Highly Complex:**
        - **Analysis:** [Break down structure]
        - **Problem Decomposition:** [Manageable sub-problems]
        - **Sub-problem Processing:** [Initial -> Reflection -> Improved for each]
        - **Integration:** [Combine solutions]
        - **Overall Reflection:** [Evaluate complete solution]
        - **Final Optimization:** [Final refinements]
        - **Summary:** [Comprehensive summary]
    </think>
    <answer>
        Provide the final solution using the following style:
        - State the goal.
        - Use numbered or bulleted transformation steps (e.g., Translate, Apply, Relabel).
        - Show the mathematical transitions clearly.
        - Conclude with: "Thus, the transformed equation is ..., making the correct answer \\boxed{{ANSWER_CHOICE}}."
    </answer>

    Problem:
    {problem}
"""