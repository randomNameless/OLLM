filepath='./responce.txt' #define responce
def check_keywords(file_path, keywords):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            
            for keyword in keywords:
                if keyword in content:
                    print('rules violation, please reevaluate')
                    return
            
            print('no violation, passed')
    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

if __name__ == "__main__":
    file_name = 'prompt_v1.txt'
    keywords_to_check = [
        'battery', 
        'system time', 
        'signal fluctuates',  
        'unchanged output structure', 
        'lack of confirmation'
    ]
    
    check_keywords(filepath, keywords_to_check)