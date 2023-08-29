likes = [459, 553, 1115, 741, 702, 307, 564, 231, 202, 150, 914, 371]
comments = [20, 24, 53, 37, 26, 16, 28, 28, 17, 17, 30, 17]

avg_likes = sum(likes) / len(likes)
avg_comments = sum(comments) / len(comments)
follwers = 20900

print('Calculated on the last 12 posts:'.upper())
print(f"The average of the likes received is {avg_likes:.2f}.")
print(f"The average of the comments received is {avg_comments:.2f}.")
print(f"About {avg_likes / follwers:.2%} of the followers of this page likes the contents and about {avg_comments / follwers:.2%} write a comment for every post.")
