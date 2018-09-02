# Typing Master
### Difficulty : Easy
### Points : 50

# Description
If you think you have it in you, connect now to 34.216.132.109 9093 and prove your mettle.

You will be presented with a simple typing task which is meant to check your typing speed.

For example, Can you type 'Z' 10 times followed by 'u' 6 times, followed by the sum of their ASCII values?

ZZZZZZZZZZuuuuuu207

# Solution

Find the letters and the no. of times they need to be printed. Add the the sum of the ASCII values.

But when I sent it, there was no flag sent back to me.

![screenshot 351](https://user-images.githubusercontent.com/42334661/44945135-2479df80-ae00-11e8-83f9-dabbedf02aac.png)

Then, I found that i forgot to add newline character **'\x0a'**.
Appending the newline character (either '\n' or '\x0a'), gave me the flag

![screenshot 352](https://user-images.githubusercontent.com/42334661/44945168-f052ee80-ae00-11e8-9de4-4742c2861d56.png)

Flag : **CodefestCTF{1_s33_y0u_4r3_a_m4n_0f_sp33d}**
