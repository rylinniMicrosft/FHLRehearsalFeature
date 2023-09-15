import webbrowser
import json
from bs4 import BeautifulSoup
import os


def createSummary(questions):
    with open('temp.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Create the "Critical Questions" summary box with a carousel
    critical_questions_box = soup.new_tag('div', attrs={'class': 'summaryBox'})
    critical_questions_title = soup.new_tag('h2', attrs={'class': 'title'})
    critical_questions_title.string = 'Critical Questions'

    # Create a div for the carousel
    carousel_div = soup.new_tag('div', attrs={'class': 'carousel'})


    # Create an unordered list to hold the questions
    question_list = soup.new_tag('ul', attrs={'class': 'question-list'})
    for question in questions:
        question_item = soup.new_tag('li')
        question_item.string = question
        question_list.append(question_item)

    # Append the title and the question list to the "Critical Questions" summary box
    carousel_div.append(question_list)
    critical_questions_box.append(critical_questions_title)
    critical_questions_box.append(carousel_div)

    # Locate the "Fillers" summary box
    fillers_summary_box = soup.find('div', {'id': 'fillerWordsSummaryBox'})

    # Insert the "Critical Questions" summary box right before the "Fillers" summary box
    fillers_summary_box.insert_before(critical_questions_box)


    # Write the modified content back to the same file
    with open('result.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    # Open the modified file in the default web browser
    webbrowser.open('file://' + os.path.realpath('result.html'))