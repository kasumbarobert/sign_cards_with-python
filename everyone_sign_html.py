
def everyone_sign(participants):

    for writer in participants:
        message = "Thank you friends";
        html_header="<html><head><title>"+writer+"'s card</title></head><body style='background-color:blue;'>"
        message_div = "<div style='width:300px;margin-left:auto; margin-right:auto;margin-bottom:400px;padding:2%; margin-top:200px; border-radius:10px; " \
                      "background-color:#efe; color:orange'>" \
                      "<h2 style='text-align:center;'>"+message+"</h2><ul style='text-align:center;list-style-type: none;padding:0;margin:0;font-family:DejaVu Sans;''>";
        for participant in participants:
            if writer != participant:
                message_div += "<li>"+participant+"</li>"
        message_div+="</ul><h3 style='color:blue;text-align:center;'>"+writer+"</h3></div>"

        html_code = html_header+message_div+"</body></html>"

        html_file = open("cards/"+writer+"_card.html","w")

        html_file.write(html_code)

everyone_sign({"See-Mong Tan",

"Victoria Kirst",

"Matthew Levine",

"Eric Breck",

"Riccardo Crepaldi"})
