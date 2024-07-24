from pypdf import PdfReader
import mimetypes
import logging
import os
import sys

import generate


if len(sys.argv) > 1:
    input_file = sys.argv[1]
    if os.path.isfile(input_file):
        filetype, _ = mimetypes.guess_type(input_file)
        #print(filetype)

        # Clear the file
        with open("user_input.txt", "w"):
            pass

        # .txt
        if filetype == "text/plain":
            generate.generate_text(input_file)
            #pass
            
        # .pdf
        elif filetype == "application/pdf":
            logging.getLogger("pypdf").setLevel(logging.ERROR)
            reader = PdfReader(input_file, strict=False)
            #num_pages = len(reader.pages)
            text_string = ""
            with open("user_input.txt", "a", encoding="utf-8") as file:
                for page in reader.pages:
                    print(page.extract_text().strip(" "), file=file)
                    #text_string += page.extract_text()
            #generate.generate_text(input_file)
            generate.generate_text("user_input.txt")
            #print(text_string)
    else:
        print("Error: not a file")
else:
    print("Error: please provide a file")
