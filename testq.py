def replace_t_with_sharp(text):
    replaced_text = text.replace("t", "#")
    return replaced_text

# OCR 결과에서 "t"를 "#"으로 대체
text = "Ct D G Ct A#"
modified_text = replace_t_with_sharp(text)
print(modified_text)
