with open("cat.jpg","rb") as f_in:
    with open("cat_copy.jpg", "wb") as f_out:
        f_out.write(f_in.read())
        