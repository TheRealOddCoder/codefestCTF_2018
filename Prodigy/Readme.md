# Prodigy
### Difficulty : Easy
### Points : 100

# Description
Self proclaimed prodigy Gourav, has just learnt about binaries and compiler. He believes he can hide anything in the binary unless he doesn't print it. Show him that he is wrong.

# Solution
Lets fire-up gdb.
The main function didn't give much information. It just showed the puts() function called.


![gdb_prodigy_1](https://user-images.githubusercontent.com/42334661/44945426-ef24c000-ae06-11e8-8287-6b2739996486.png)


The puts() function didn't show promise.


![gdb_stack](https://user-images.githubusercontent.com/42334661/44945436-2c894d80-ae07-11e8-913a-a9ad73725291.png)


This means the flag is somewhere else. Objdump revealed an interesting function getFlag()


![getflag](https://user-images.githubusercontent.com/42334661/44945458-930e6b80-ae07-11e8-8a23-f509427fb848.png)


Setting breakpoint at the start of the program and going into the getFlag(), the flag is present in the stack.




