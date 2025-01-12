# Information Security Challanges
Lecture 0

Challenge 0.1 (Simple): Find the login/password combination used in Lab 0's scavenger hunt.
Challenge 0.2 (Normal): Write a script (or a one-liner) that finds all the clues at once in Lab's 0 scavenger hunt.
Lecture 1

Challenge 1.1 (Simple):
D_AZ_5H7S006_9WHF6BHD_33HX_5
VHSAH3WS0AHIJHX3SY0H064WH6XH
AZW4HS9WHX_3WH5S4WVHX3SYH5HT
BAH064WA_4W0HAZWHX3SYH_0HZ_V
VW5H_5HS56AZW9HX_3WHAZ_0H4W0
0SYWH_0HAZWHS50DW9HA6HUZS33W
5YWHIHV6AHI
Challenge 1.2 (Normal): Decrypt the file 'Challenge-1.2'. Hint: It has been encrypted with a key 120bits long, but the file starts with the string "Challenge 1.2" (The plain text is in ascii. Make sure you're not using another encoding when attempting to read the decrypted version.)
Lecture 2

Challenge 2.1 (Hard): Length Extension Attack:
Extend the following message: "I give you the following amount of SEK coded in binary:\x12". (The message is encoded in ascii.)
"HMAC" follows the insecure pattern h(key | msg), the hash function is SHA-1. The key length is 7 bytes long. (Don't bruteforce it!)
HMAC = 67452301EFCDAB8998BADCFE10325476C3D2E1F0.
You need to produce a message extend the number coded in binary in the given message, and produce a valid "HMAC" = h(key | extended_msg).
You do not know the key.
Challenge 2.2 (Simple): Verify the HMACs
Key_1: "1234", Key_2: "5678", HMAC follows the pattern h(key_2 | h(key_1 | msg)), the hash function is SHA-1. The inner hash is used an ascii string. So computing the second hash should look like h("56785aa5787118c3816d7f80c497d557176fae450b93").
Message 1: "Challenge 2.2 is easy." HMAC: 12d44a1c2448cc54ddffc75e69313a7964d5d775
Message 2: "Challenge 2.2 is doable." HMAC: 1b25d0e281f73935f7a122c088c1bc34686b271b
Message 3: "Challenge 2.2 is hard." HMAC: aec64e480f251c6811686597305b04edcc25da35
Which (if any) of these messages have been tampered with.
Challenge 2.3 (Normal): Send me an email encrypted with PGP:
Read about Web of Trust.
Get my public key from NextILearn.
Send me an email (encrypted with my public key) including a link to a source on Web of Trust and your public key.
The email's subject must be "[INTSEC] Challenge 2.3".
Upload your public key on https://keyserver.ubuntu.com
I will answer you using your public key, giving you the secret to put as an answer for the challenge.
Lecture 3

Challenge 3.1 (Normal): Break weak passwords (with no salt)
 They follow the format: Hash-Algo, Hash, Hint
SHA1, 30139264c3ec85759ce4f83c2fe286ecb63e6d43, PIN code
md5, c49078e81caafab96c08390197cf6a96, you need to find the right key(s)
SHA-256, b81848b9e4857c5ed8da601fa6ba92d9c2ee6c6aceabcf5e09813b427dab7bfc, Common password
Challenge 3.2 (Normal): Break weak passwords with salt h(Salt | password)
Hash-Algo, Hash, Salt, Hint
SHA1,57536215cfe9781d21733fcab27a653e9db92577,1fa6,PIN code
SHA-256,8421f0e3432bb339f3671341bc1ec96f6eb283dbf65bb56793065458c20cf945,cb63, L1tera11y a password
md5,e75a0b86d4f30e2e56a73cbe9d7dbf07,e098, You need to know something (obvious) about me.
Challenge 3.3 (Normal): Benchmark
Try to compute 1000 hashes of any random values with: (MD5, SHA-1, SHA-256, Argon2id)
How many attempt could you make in a month for each? (Let me know if you used a GPU.)
Lecture 4

Challenge 4.1 (Simple):
Fictional scenario: Imagine I wrote a game for the student of the course. I put it on a linux server where all students have an account and are part of the group students. Here are the files related to the game:
- _ _ _ _ _ _ _ _ _ nicolas students game-binary
- _ _ _ _ _ _ _ _ _ nicolas students high-scores.txt
Set the rights to let anyone in the group "students" play the game and save their best score, without allowing anyone to cheat. (Apply the principle of least privilege and Fail-safe defaults). You can assume that a process regularly saves and flushes the content of high-scores.txt. (Credit for this problem: Alan Davidson.)
Challenge 4.2 (Simple):
Go read the sources of Samy and/or the explanations of its author to answer the following questions:
Myspace prevented users to add most html tags such as <script>, where did Samy put his code?
Myspace prevented user to use essential keywords of javascript such as innerHTML, how did Samy bypassed this limitation?
Write a one-sentence explanation for each of these questions.
Lecture 5:

Challenge 5.1 (Hard): Quine
Write a quine in the language of your choice. (Not a trivial quine like "1".)
Don't cheat! If you look for the solution online, you will never again have the opportunity to find it on your own.
If you succed you should be able to run your program, save the output in a file, run this new program, save its output in a file, run, etc and the files should be the same. (Do test it!)
Then you can read Reflections on trusting trust, it's only 3 pages, and it's brilliant.
Challenge 5.2 (Normal): Checking binaries
Write a short script that takes two directories as input.
For each files in one directory, check that there is another file of the same name in the other directory.
Compute a checksum for each files, and compare.
Challenge 5.3 (Normal): Tests
Write 2 to 3 tests for the XOR encryption function you
used in Challenge 1.2 (even if you used an external
service).
Test the full extent of possible input characters.
Use a unit test framework.
Put in the comments which part is the initialization,
function under test, and oracle.
Let me know if you found a bug.
Lecture 6

Challenge 6.1 (Hard):
Consider the implementation of indoor security cameras within a household shared by a multi-age family, consisting of members from different age groups. Identify and describe potential security and privacy concerns that may arise due to the presence of such technology. Consider the possible flaws or shortcomings in the design of the camera system, focusing on what might go wrong when deployed in a family setting. From a human-centred perspective, think how these concerns might impact different members of the household, particularly considering generational differences.
Apply both human-centred principles and a feminist perspective to explore the situation. Identify and suggest at least one practical/technical solution that addresses these concerns you have outlined.
Note that avoiding the use of the camera entirely is not an option or
solution.
Write your propositions in a separate pdf. (You should metion the pdf name in your csv.)
Lecture 7:

Challenge 7.1 (Normal): SQL injection
Run sqli-dojo (Link)
Get the secret value from the "GET parameter injection in the middle of a parameter" page.
Write in your csv the series of SQL injections you needed to perform to obtain the secret value.
Challenge 7.2 (Hard): Find the backdoor in passoire's original image. (And no I don't mean just the suspicious user, even though it's related.) You can work on this one with your group, but you all need to submit individually the answer. (I'm expecting detailed explanations if you want the 3 points here.)
