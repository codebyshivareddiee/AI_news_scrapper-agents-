#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from crew import AiNews

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'openai',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    }

    # inputs_array = [
    #     {
    #         'topic': 'ai agents',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     }, 
    #     {
    #         'topic': 'openai',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     },
    #     {
    #         'topic': 'hugging face',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     }
    # ]

    AiNews().crew().kickoff(inputs=inputs)

run()