import os
import openai
from flask import Flask,jsonify                   # Flask imported hai for web if you ..

openai.api_key ="API_key_aapna_dalo"              # aapna Api key use karo

#gpt_?? idhar koi vi model lelo.
def Hallo_mr_Bita(Prompt):
  response = openai.chat.completions.creat(
      model="gpt-??" ,      
      messages =[{"role":"user","content": Prompt}]
      )  

  return response.choicse[0].message.content.strip()
  
  
if __name__=="__main__":
    while True:
        user_input =input("tuu: ")
        if user_input.lower() in ["quit","exit"]:
            break
        
        response = Hallo_mr_Bita(user_input)
        print("Bitabot:",response)
         
