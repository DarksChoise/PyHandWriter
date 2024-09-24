def get_line_height(font):
    bbox = font.getbbox("A")
    return bbox[3] - bbox[2]


def split_line(text, draw, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        if current_line:
            test_line = current_line + " " + word
        else:
            test_line = word

        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_width = bbox[2] - bbox[0]

        if line_width > max_width:
            if draw.textbbox((0, 0), word, font=font)[2] - draw.textbbox((0, 0), word, font=font)[0] > max_width:
                split_word = ""
                for char in word:
                    test_word = split_word + char
                    bbox_word = draw.textbbox((0, 0), test_word, font=font)
                    word_width = bbox_word[2] - bbox_word[0]

                    if word_width > max_width:
                        lines.append(split_word)
                        split_word = char
                    else:
                        split_word = test_word

                if split_word:
                    current_line = split_word
            else:
                lines.append(current_line)
                current_line = word
        else:
            current_line = test_line

    if current_line:
        lines.append(current_line)

    return lines
