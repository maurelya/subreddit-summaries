import os
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

from data.emotions import get_emotion_list

# API key you created
ibm_api_key = os.environ['IBM_API_KEY']

# Project ID of your watsonx instance
watsonx_project_id = os.environ['WATSONX_PROJECT_ID']

# URL service endpoint
ibm_cloud_url = os.environ['IBM_CLOUD_URL']

creds = { "url": ibm_cloud_url, "apikey": ibm_api_key }

def send_to_watsonxai(prompt,
                    model_name="google/flan-ul2",
                    decoding_method="greedy",
                    max_new_tokens=100,
                    min_new_tokens=30,
                    temperature=1.0,
                    repetition_penalty=2.0
                    ):
    '''
   helper function for sending prompts and params to Watsonx.ai
    
    Args:  
        prompts:list list of text prompts
        decoding:str Watsonx.ai parameter "sample" or "greedy"
        max_new_tok:int Watsonx.ai parameter for max new tokens/response returned
        temperature:float Watsonx.ai parameter for temperature (range 0>2)
        repetition_penalty:float Watsonx.ai parameter for repetition penalty (range 1.0 to 2.0)

    Returns: None
        prints response
    '''

    # Instantiate parameters for text generation
    model_params = {
        GenParams.DECODING_METHOD: decoding_method,
        GenParams.MIN_NEW_TOKENS: min_new_tokens,
        GenParams.MAX_NEW_TOKENS: max_new_tokens,
        GenParams.RANDOM_SEED: 42,
        GenParams.TEMPERATURE: temperature,
        GenParams.REPETITION_PENALTY: repetition_penalty,
    }


    # Instantiate a model proxy object to send your requests
    model = Model(
        model_id=model_name,
        params=model_params,
        credentials=creds,
        project_id=watsonx_project_id)

    return model.generate_text(prompt)



def summarize_augment( template_in, subreddit, title, post_body, top_comment ):
    return template_in % ( subreddit, title, post_body,  top_comment )          



'''
function to summarize the top post and comments.
'''
def summarize_post(subreddit, title, post_body, top_comment):

    prompt_template = """
    The following is a post from the %s subreddit.
    Read the title, post and top comment and then write a short 1 paragraph summary.

    Title: %s
    Post: %s
    Top comment: %s

    Summary:

    """
    augmented_prompt = summarize_augment(prompt_template, subreddit, title, post_body, top_comment)

    #print("\n augmented_prompt: ", augmented_prompt)

    return send_to_watsonxai(prompt=augmented_prompt,
                    model_name="google/flan-ul2",
                    decoding_method="greedy",
                    max_new_tokens=1000,
                    min_new_tokens=50,
                    temperature=2.0,
                    repetition_penalty=2.0)


def sentiment_augment( template_in, subreddit, emotion_list, summary ):
    return template_in % ( subreddit, emotion_list, summary )  



'''
function to get the sentiment of a reddit post.
'''
def sentiment_analysis(subreddit, summary):

    prompt_template = """
    The following is a summary of a post from the %s subreddit.
    Read the summary and classify the summary with a human emotion from the following list:
    %s

    Summary: %s

    Classification: 

    """
    augmented_prompt = sentiment_augment(prompt_template, subreddit, get_emotion_list(), summary)

    #print("\n augmented_prompt: ", augmented_prompt)

    return send_to_watsonxai(prompt=augmented_prompt,
                    model_name="google/flan-ul2",
                    decoding_method="greedy",
                    max_new_tokens=5,
                    min_new_tokens=0,
                    temperature=2.0,
                    repetition_penalty=1.0)