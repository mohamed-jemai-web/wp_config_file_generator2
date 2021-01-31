wp=open('wp.php')
config = []
wp_full =[]
for line in wp:
    new_val = ""
    if line.startswith('define'):


        st1 = line.find("'")
        sp1= line.find("'",st1+1)

        par = line[st1+1:sp1]

        st2 = line.find("'",sp1+1)
        sp2 = line.find("'", st2 + 1)

        val = line[st2+1:sp2]

        new_val = input("Enter "+ par +"[" + val + "]: ")




    else:
        par=""
        val=""


    config += [[line,par, val, new_val]]
wp_new = ""
for line in config:

    txt =str(line[0])
    if line[3] !="":
        #print(txt)
        txt = txt.replace(line[2],line[3])
        #print(txt)
    wp_new+=txt
    #print(wp_new)
    #print(config)
try:
    wp2=open('wp_new.php','x')
except:
    wp2=open('wp_new.php','w')
wp2.write(wp_new)





