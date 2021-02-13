my_string = "Hello world! This is a very, very long string. \
Even though this string is on three different lines, it should \
print as one line. Notice how the line breaks are different. \
That is pretty neat"
print(my_string)

print()

long_string = """Notice how this weird looking
    string is being
        printed."""
print(long_string)


string = """               *
           ***
          *****
         *******
          *****
           ***
            *"""

print(string)

print()

my_string = "The brown dog jumps over the lazy fox." #slice function
my_slice = my_string[4:9]

print(my_slice)

stringo = "Hellow \u041b World"
print(stringo)

max_str = "xyzZ.?!"
#num =len(max_str)
#print(num)
print(max(max_str))
print(min(max_str))


print()
print()

################################################ Methods

string1 = "Hello world"
string2 = "world"
print(string1.strip(string2))



