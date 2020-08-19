likes = {}
comments = {}

while True:
    cmd_input = input()
    if cmd_input == "Log out":
        break

    args = cmd_input.split(": ")
    cmd =  args[0]
    username = args[1]

    if cmd  == 'New follower':

        if username in likes:
            continue
        likes[username] = 0
        comments[username] = 0
    elif cmd == 'Like':
        count = int(args[2])
        if username not in likes:
            likes[username] = 0
            comments[username] = 0
        likes[username] += count
    elif cmd == 'Comment':

        if username not in comments:
            likes [ username ] = 0
            comments [ username ] = 0
        comments[username] += 1
    elif cmd == 'Blocked':
        if username not in likes:
            print(f"{username} doesn't exist.")
        else:
            likes.pop(username)
            comments.pop(username)

print(f"{len(likes)} followers")
sorted_likes = dict(sorted(likes.items(), key=lambda u: (-u[1], u[0])))
for user, likes in sorted_likes.items():
    print(f"{user}: {likes+ comments[user]}")
