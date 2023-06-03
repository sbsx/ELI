# import required libraries
import sys
import tweepy
import csv


# import file with auth keys keywords
import AuthKeys

"""
Important Data:
    - User Name
    - User Screen Name
    - User id
    - User bio?
    - User mentions?
    - Tweet Content
    - Tweet id
    - Creation date
    - Reply, retweet, and favorite count?

    - Lang? (if we wish to expand to other languages)

CSV Structure:

Tweet id | Tweet Content | Created At | User id | User Name | User Screen Name | ?[User bio, Metrics(replay, retweet favorite)]



"""


def main(argv):
    # argv is a list of twitter links
    print("---------------------------------------")

    print('Number of arguments:', len(argv), 'arguments.')
    print('Argument List:', str(argv))

    # Authenticate User
    auth = tweepy.OAuth1UserHandler(
        AuthKeys.API_KEY, AuthKeys.API_KEY_SECRET, AuthKeys.ACCESS_TOKEN, AuthKeys.ACCESS_TOKEN_SECRET
    )

    # Retrieve API
    api = tweepy.API(auth)
    _id_list = []
    # Open CSV for writing
    with open('data.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Tweet ID", "Tweet Content", "Created At",
                        "User ID", "User Name", "User Bio", "User Screen Name"])

        # Process tweets
        for url in argv:
            # Parse and grab url ID
            _id = url.split('/')[-1].split('?')[0]

            # Store in new list of id(s)
            _id_list = [_id]
            print(_id)

            print("---------------------------------------")
            # Look up tweets
            test_tweets = api.lookup_statuses(
                id=_id_list, tweet_mode="extended")
            if (len(test_tweets) == 0):
                print("Failed to look up tweet. Check if tweet id is correct.")
                exit()

            # Printing the statuses
            print("         ::::::::::::::: ", test_tweets)
            for status in test_tweets:
                print("Created At: " + str(status.created_at))
                print("Tweet ID: " + str(status.id))
                print("")
                print("User ID: " + str(status.user.id))
                print("User name: " + str(status.user.name))
                print("User screen name: " + str(status.user.screen_name))
                print("User Bio: " + str(status.user.description))
                print("")
                print("Tweet Contents: \n" + status.full_text)
                print("---------------------------------------")

                row = [str(status.id), str(status.full_text), str(status.created_at), str(
                    status.user.id), str(status.user.name), str(status.user.description), str(status.user.screen_name)]
                writer.writerow(row)

                """
                print("The status " + str(status.id) +
                    " is posted by " + status.user.screen_name + "\n")
                print("This status says : \n\n" + status.text, end="\n\n")
                """


if __name__ == "__main__":
    main(sys.argv[1:])
