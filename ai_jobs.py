from flask import Flask, render_template, jsonify

import random

import matplotlib.pyplot as plt

import io

import base64

 

app = Flask(__name__)

 

industries = ["Tech","Automotive","Health","Agriculture","Transportation","Security","Civil Rights","Law"]

age_groups = ["Students (18-22)", "Employees (25-55)", "Seniors (56-70)"]

 

def generate_ai_impact():

    data = []

    for industry in industries:

        ai_replacement = round(random.uniform(10,20), 2) #Percentage in how big the impact it will be in : %

        new_oportunities = round(ai_replacement * 0.4, 2) #40 % people will be upskilled to new technologies

        impact_by_age = {age: round(random.uniform(10, 20), 2) for age in age_groups }

        data.append({

            "industry": industry,

            "ai_replacement": ai_replacement,

            "new_opportunities": new_oportunities,

            "impact_by_age": impact_by_age

        })

    return data

 

def generate_pie_chart():

    labels = ["Ready (99.9%)", "To Be Learnd On The Job (1%)"]

    sizes = [99.9, 1]

    colors = ["blue", "green"]

    explode = (0.1, 0)

   

    fig, ax = plt.subplots()

    ax.pie(sizes, explode=explode, labels=labels,colors=colors,autopct='%1.1f%%',startangle=90)

    ax.axis('equal')

   

    img = io.BytesIO()

    plt.savefig(img,format='png')

    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return plot_url

 

@app.route('/')

def home():

    plot_url = generate_pie_chart()

    return render_template('index.html', plot_url=plot_url)

 

@app.route('/data')

def get_data():

    data = generate_ai_impact()

    we_work_for_you = {'description':'A description for a dedicated team that looks in their employees the right needs to prepaire them for next chapter of technology progress.'}

    return jsonify({"industries": data, "we_work_for_you": we_work_for_you})

 

 

if __name__ == '__main__':

    app.run(debug=True)