financial_data = {
    "Microsoft": {"Total Revenue": "198B", "Net Income": "72B", "Total Assets": "411B"},
    "Apple": {"Total Revenue": "394B", "Net Income": "99B", "Total Assets": "352B"},
    "Tesla": {"Total Revenue": "81B", "Net Income": "12B", "Total Assets": "83B"}
}

def simple_chatbot():
    print("Welcome to the Financial Chatbot! Ask about revenue, net income, or assets.")
    while True:
        user_query = input("Enter your question (or type 'exit' to quit): ").lower()
        
        if "revenue" in user_query:
            company = input("Which company? (Microsoft/Apple/Tesla): ")
            print(f"Total revenue of {company} is {financial_data[company]['Total Revenue']}")
        
        elif "net income" in user_query:
            company = input("Which company? (Microsoft/Apple/Tesla): ")
            print(f"Net income of {company} is {financial_data[company]['Net Income']}")

        elif "assets" in user_query:
            company = input("Which company? (Microsoft/Apple/Tesla): ")
            print(f"Total assets of {company} are {financial_data[company]['Total Assets']}")

        elif user_query == "exit":
            print("Goodbye!")
            break

        else:
            print("Sorry, I can only answer predefined financial queries.")


simple_chatbot()
