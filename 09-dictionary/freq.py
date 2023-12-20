def lyric_to_freq(song):
    # create an empty dictionary where its key would be the word and its value the count number.
    song_dict = {}
    # iterate over song
    for word in song:
        # if word already in dictionary, add to its value 1
        if word in song_dict:
            song_dict[word] = song_dict[word] + 1
        # if the word is not there, set the word as a key and 1 as its value.
        else:
            song_dict[word] = 1
    # after finishing the loop, return the dictionary.
    return song_dict

def most_common_word(lyrics_freq):
    values = lyrics_freq.values()
    max_value = max(values)
    words = []
    
    for word in lyrics_freq:
        if lyrics_freq[word] == max_value:
            words.append(word)
    return (words, max_value)

def words_count_we_want(song, min_times):
    result = []
    while True:
        common = most_common_word(lyric_to_freq(song))
        if common[1] > min_times:
            result.append(common)
            for w in common[0]:
                song.remove(w)
        else:
            break
    return result

song = ["he", "she", "he", "she", "football"]
min_times = 1
print(words_count_we_want(song, min_times))
