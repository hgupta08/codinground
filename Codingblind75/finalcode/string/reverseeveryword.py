def reverseWords(string):
    st = []
    result = ""

    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])
        else:
            while st:
                result += st.pop()
            result += " "

    # Reverse the last word (if any)
    print(st)
    while st:
        result += st.pop()

    return result


# Driver Code
if __name__ == "__main__":
    string = "Geeks for Geeks"
    print(string[::-1])
    print(reverseWords(string))
