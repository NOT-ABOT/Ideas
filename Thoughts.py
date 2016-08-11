#A compilation of things to add to my Reddit bots. 


#I like this for checking the age of the posts. I should use this in the UnknownVideosMod bot
now = datetime.now(timezone.utc).timestamp()
if now - submission.created_utc < POST_TIME:
    continue
    
#Use urllib.parse, too, as this is more efficient
    

