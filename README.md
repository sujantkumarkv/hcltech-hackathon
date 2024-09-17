> It was required to meet chatbot with a thousand examples of user complaint feedback data of a bank and given some churn data as well. 

OpenAI API was used and first it is required to find the category of based on the users query. 
So firstly I use pydantic and like there is a json. It ensure that to check that the return type of the LLM is of a certain type. 
So I make a JSON which is basically just the category and the confidence as a float number that would be returned.
```json
{
        "category": "Online Banking",
        "confidence": 0.9
}
```
I use a GPT-4 mini model like a small model just to find the category. You can technically also use some classification algorithms here or models but like since LLMs since models have generally become very general purpose and useful so that is almost a solved problem and we can directly use models for so many of these tasks if prompted correctly.  

So I use that and after that taking the category I then create a main mega prompt which includes like the category and one more thing is this is dynamic prompting so if the user says eg,

> "my savings account has not been put interest rates are a little bit confusing" 

so it sees if "savings" and "account" and based on that it will pick up the values from the excel file as data points and then it will add that to the prompt as well so now the prompt has a context of that users feedback, lets say, it's credit cards and it's a monthly and yearly balance coupled with the category of the feedback and then the model responds with helping the users query feedback.

I use GPT-4o model for this as it's a bigger than GPT-4o mini and and then I went ahead with testing & converting 50 examples from spreadsheet data to CHATBOT'S response. I created new CSV and excel files for it in the `data/` folder.

### For churn :

since the data is already given churn as an yes/no data points so what I did was to find basically the correlation and which points correlate with that select rate cards monthly and yearly balances and something like that so you can take those data and find correlation heat map heat matrix like using sklearn and standard like standard procedures how for these data I just you know remove to the empty and null values replace them and yeah I just plotted them so and I have the pictures of those.