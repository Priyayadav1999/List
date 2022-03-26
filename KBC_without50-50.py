print("Kaun Banega Crorepati mein aapka swagat hain")
q_list=[["how many continents are there?"],
        ["What is the capital of India?"],
        ["NG mein kaun sa course karaya jata hai?"]]
opt_list=[["four","nine","seven","eight"],
         ["chandigarh","bhopal","chennai","delhi"],
         ["software engineering","counseling","tourism","agriculture"]]
sol_list=[3,4,1]
i=0
count=0
while i<len(q_list):
    print("this is your question:-")
    print(q_list[i])
    print("those are your option:-")
    j=0
    c=1
    while j<len(opt_list[i]):
        print(c,opt_list[i][j])
        j=j+1
        c=c+1
    sol=int(input("enter your option solution"))
    if sol==sol_list[i]:
        print("congrats")
        count=count+1
    elif sol!=sol_list:
        print("you lose")
        break
    i=i+1
    if count==len(q_list):
        print("badhaai ho!,Aap Crorepati ban gaye hain")
