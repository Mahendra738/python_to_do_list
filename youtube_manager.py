import json

def load_data():
    try:
        with open('data.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def data_save_helper(videos):
    with open('data.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print('\n')
    print("*" * 50)
    
def add_videos(videos):
    name = input("enter the name: ")
    time = input("enter the duration: ")
    videos.append({'name': name, "time": time})
    data_save_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the vodio number you want to update: "))
    if 1 <= index <= len(videos):
        name = input("enter the name: ")
        time = input("enter the time: ")
        videos[index - 1] = {'name': name, 'time': time}
        data_save_helper(videos)
    else:
        return "invalide index selected :| "

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("enter the video numnber to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        data_save_helper(videos)
    else: 
        return "invalide index selected :| "

def main():
    videos = load_data()
    
    while True:
        print("\n Youtube manager | choose an option ")
        print("1. list all the youtube video")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delate a youtube video")
        print("5. Exit the app")
        choice = input("Enter the choice: ")
        # print(videos)

        match choice:
            case '1': 
                list_all_videos(videos)
                
            case '2':
                add_videos(videos)
                
            case '3':
                update_videos(videos)
                
            case '4':
                delete_videos(videos)
                
            case '5':
                break
            
            case _:
                print("invalid choise :|")
                
if __name__ == '__main__':
    main()