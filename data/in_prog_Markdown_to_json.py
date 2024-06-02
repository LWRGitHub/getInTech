import re
import json

class Markdown_to_json:

    def __init__(self):
        pass

    def markdown_to_json(self, context):
        # print("here")
        how_to = []

        def remove_empty_lines(markdown_list):
            in_code_block = False
            cleaned_list = []

            for line in markdown_list:
                if line.strip().startswith('```'):
                    in_code_block = not in_code_block
                    cleaned_list.append(line)
                elif not in_code_block and not line.strip():
                    continue
                else:
                    cleaned_list.append(line)

            return cleaned_list

        # split contest["markdown_how_to_solve"] at \n to get the list of lines
        # also remove any empty lines unless in a code block
        markdown_list = context["markdown_how_to_solve"].split("\n")
        f = open('markdown_list_1.json', 'w', encoding="utf-8")
        json.dump(markdown_list, f, indent=4)
        f.close() 

        markdown_list = remove_empty_lines(markdown_list)

        # print(markdown_list)

        f = open('markdown_list_2.json', 'w', encoding="utf-8")
        json.dump(markdown_list, f, indent=4)
        f.close()         

        # find all pairs🍐 of a * | ** | *** in a string
        def find(s):
            patterns = {
                3: r'\*\*\*[^*]+\*\*\*',
                2: r'\*\*[^*]+\*\*',
                1: r'\*[^*]+\*'
            }
            
            result = []
            i = 0
            while i < len(s):
                match = None
                for type_, pattern in patterns.items():
                    regex = re.compile(pattern)
                    current_match = regex.match(s, i)
                    if current_match:
                        match = {'type': type_, 'idxs': [current_match.start(), current_match.end() - 1]}
                        break
                
                if match:
                    result.append(match)
                    i = match['idxs'][1] + 1
                else:
                    i += 1
            
            return result
    
        # find all pairs🍐 of ` in a string
        def find_back_ticks(s):
            patterns = {
                1: r'`[^`]+`'
            }
            
            result = []
            i = 0
            while i < len(s):
                match = None
                for type_, pattern in patterns.items():
                    regex = re.compile(pattern)
                    current_match = regex.match(s, i)
                    if current_match:
                        match = {'type': type_, 'idxs': [current_match.start(), current_match.end() - 1]}
                        break
                
                if match:
                    result.append(match)
                    i = match['idxs'][1] + 1
                else:
                    i += 1
            
            return result

        # check if line starts with >
        # if so get indent
        def bd_callout(markdown_list, idx):
            html_data = {}

            if markdown_list[idx][0:1] == '>':
                html_data["bd_callout"] = {}

                if markdown_list[idx][0:2] == '>>':
                    if markdown_list[idx][0:3] == '>>>':
                        html_data["bd_callout"]["indent"] = 3
                    else:
                        html_data["bd_callout"]["indent"] = 2
                else:
                    html_data["bd_callout"]["indent"] = 1

            # remove all > from the front of the line
            markdown_list[idx] = markdown_list[idx].lstrip('>')

            return html_data
        prior_line_has_callout = False

        # check if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
        def if_need_add_callout_line(prior_line_has_callout, how_to, html_data):
            if prior_line_has_callout and "bd_callout" in html_data:
                    
                # check if str, list or dict
                if type(how_to[-1]["content"]) == list:
                    how_to[idx-1]["content"].append([*how_to[idx-1]["content"], html_data])
                else: # type(how_to[-1]["content"]) == str or type(how_to[-1]["content"]) == dict
                    how_to[idx-1]["content"].append([how_to[idx-1]["content"], html_data])

        # order data acording to Md `
        def sort_buld_sm_code_block(data, ch_idxs):
            code_data = {}
            
            code_data["tag"] = "span"
            code_data["content"] = []

            if ch_idxs[0]["idxs"][0] != 0:
                content = data[0:ch_idxs[0]["idxs"][0]]
                code_data["content"].append({
                    "tag": "span",
                    "content": content
                })

            # loop through ch_idxs
            last_i2 = None
            for code_info in ch_idxs:
                [i1, i2] = code_info["idxs"]

                # if last_i2 is not None add the text between the last_i2 and i1 to the list
                if last_i2 != None:
                    content = data[last_i2:i1]
                    code_data["content"].append({
                        "tag": "span",
                        "content": content
                    })

                content = data[i1+1:i2]
                code_data["content"].append({
                    "tag": "code",
                    "content": content
                })

                last_i2 = i2 + 1


            # if last the last list in ch_idxs at index 1 is not the last index of text add the text between the last_i2 and the end of the text to the list
            if last_i2 != None and last_i2 < len(data):
                content = data[last_i2:]
                code_data["content"].append({
                    "tag": "span",
                    "content": content
                })
            
            return code_data

        # order data acording to Md * | ** | ***
        # **Trie Initialization (`__init__` method)**
        # Trie **Initialization** (`__init__` method)
        def sort_buld_italic(text, ch_idxs):
            astrict_data = {}

            astrict_data["tag"] = "span"
            astrict_data["content"] = []

            def has_backticks(content):
                # if even instances of ` 
                if content.find('`') != -1 and content.count("`") % 2 == 0:
                    ch_idxs = find_back_ticks(content)
                    content = sort_buld_sm_code_block(content, ch_idxs)
                return content

            
            if ch_idxs[0]["idxs"][0] != 0:
                content = text[0:ch_idxs[0]["idxs"][0]]

                # if even instances of ` 
                content = has_backticks(content)

                astrict_data["content"].append({
                    "tag": "span",
                    "content": content
                })
            #     astrict_data["tag"] = "span"
            # elif text[0] == "***":

            # loop through ch_idxs
            last_i2 = None
            for astrict_info in ch_idxs:
                [i1, i2] = astrict_info["idxs"]
                astrid_count = astrict_info["type"]

                # if last_i2 is not None add the text between the last_i2 and i1 to the list 
                if last_i2 != None:
                    content = text[last_i2:i1]

                    # if even instances of ` 
                    content = has_backticks(content)

                    astrict_data["content"].append({
                        "tag": "span",
                        "content": content
                    })
                    
                if astrid_count == 3:
                    content = text[i1+3:i2-2]

                    # if even instances of ` 
                    content = has_backticks(content)

                    # add the text between i1 and i2 to the list as a bold tag
                    astrict_data["content"].append({
                        "tag": "strong",
                        "content": {
                            "tag": "em",
                            "content": content,
                        }
                    })
                else:
                    content = text[i1+astrid_count:i2-astrid_count+1]

                    # if even instances of ` 
                    content = has_backticks(content)

                    # add the text between i1 and i2 to the list as a bold tag
                    # astrict_data["tag"] = "strong" if astrid_count == 2 else "em"
                    astrict_data["content"].append({
                        "tag": "strong" if astrid_count == 2 else "em",
                        "content": content
                    })

                
                    
                last_i2 = i2 + 1  
            
            # if last the last list in ch_idxs at index 1 is not the last index of text add the text between the last_i2 and the end of the text to the list
            if last_i2 != None and last_i2 < len(text):
                content = text[last_i2:]

                # if even instances of ` 
                content = has_backticks(content)

                astrict_data["content"].append({
                    "tag": "span",
                    "content": content
                })

            return astrict_data
        
        # make html list data >>> ol | ul
        def make_html_list_data(html_data, markdown_list, idx, prior_line_has_callout, how_to, depth):
            
            li_data = {}
            li_data["tag"] = "ol" if markdown_list[idx].lstrip()[0].isnumeric() else "ul"
            li_data["content"] = []

            # use to keep track of the parent type (e.g. ol | ul) incase of children so onece the children are done we can continue with the sibling node of the parent
            main_old_idx = idx 
            is_ol_main = "ol" if li_data["tag"] == "ol" else "ul" 
            
            # while not empty line and starts with number immediately followed by '.' or starts with space(s) then number immediately followed by '.'
            def make_li_tags(idx, markdown_list, depth, li_data):

                # while current is <li> 
                while (
                        (
                            idx < len(markdown_list) 
                            and 
                            len(markdown_list[idx]) > 0 
                            and 
                            markdown_list[idx] != ''
                        ) 
                        and 
                        (
                            markdown_list[idx].lstrip() != ''
                            and
                            (
                                markdown_list[idx].lstrip()[0] == '-' 
                                or 
                                (
                                    markdown_list[idx].lstrip()[0].isnumeric() 
                                    and 
                                    markdown_list[idx].lstrip()[1] == '.') 
                                or 
                                (
                                    markdown_list[idx].lstrip()[0:2].isnumeric() 
                                    and 
                                    markdown_list[idx].lstrip()[2] == '.'
                                ) 
                                or 
                                len(markdown_list[idx]) - len(markdown_list[idx].lstrip()) > 0
                            )
                        )
                    ):


                    spaces = len(markdown_list[idx]) - len(markdown_list[idx].lstrip())

                    # if line spaces in front of the number make sub list
                    if spaces > depth:

                        content_res, idx = make_html_list_data(html_data, markdown_list, idx, prior_line_has_callout, how_to, spaces)
                        li_data["content"].append(content_res)
                        idx += 1
                        
                        continue

                    elif spaces < depth:
                        return [idx, li_data]
                    
                    rm_count = 0
                    
                    # remove the number and the '.' or the '-' and the spaces
                    if markdown_list[idx].lstrip()[0] == '-' or (markdown_list[idx].lstrip()[0].isnumeric() and markdown_list[idx].lstrip()[1] == '.') or (markdown_list[idx].lstrip()[0:2].isnumeric() and markdown_list[idx].lstrip()[2] == '.'):

                        if markdown_list[idx].lstrip()[0] == '-':
                            rm_count = 2
                        elif markdown_list[idx].lstrip()[0].isnumeric():
                            rm_count = 3
                            # if the number is greater than 9
                            if markdown_list[idx].lstrip()[2] == '.':
                                rm_count = 4
                            # if the number is greater than 99
                            elif markdown_list[idx].lstrip()[3] == '.':
                                rm_count = 5

                        data = markdown_list[idx].lstrip()[rm_count:]

                        # check if even instances of ** are present in the line
                        if data.find('*') != -1 and data.count("*") % 2 == 0:
                            ch_idxs = find(data)
                            data = sort_buld_italic(data, ch_idxs)
                        elif data.find('`') != -1 and data.count("`") % 2 == 0:
                            ch_idxs = find_back_ticks(data)
                            data = sort_buld_sm_code_block(data, ch_idxs)
                            
                        # make {tag: li, content: data}
                        li_data["content"].append({
                            "tag": "li",
                            "content": data,
                        })
                    else:

                        data = markdown_list[idx].lstrip()
                        in_side_li_html_data = {}

                        # check if code block e.g. ``` 
                        if data.find("```") != -1:
                            # loop through the list until the next ``` is found
                            idx += 1
                            # make {tag: code, content: code}
                            in_side_li_html_data["tag"] = "fenced_code_block"
                            in_side_li_html_data["content"] = '\n'

                            # loop through code_lines and add each line to the content keep indentations "space(s)" the same
                            while idx < len(markdown_list) and data.find("```") == -1:
                                in_side_li_html_data["content"] += f"{data}\n"
                                idx += 1

                            # if prior_line_has_callout & "bd_callout" in in_side_li_html_data add to last dict in how_to
                            if_need_add_callout_line(prior_line_has_callout, how_to, in_side_li_html_data)
                            
                        # check if line starts with # | ## | ### followed by a space
                        elif data[0] == "#":
                            symbol_count = 1
                            if data[0:2] == "##":
                                if data[0:3] == "###":

                                    symbol_count = 3
                                    in_side_li_html_data["tag"] = "h5"
                                else:
                                    symbol_count = 2
                                    in_side_li_html_data["tag"] = "h4"
                            else:
                                in_side_li_html_data["tag"] = "h2"
                            
                            in_side_li_html_data["content"] = f"{data[symbol_count+1:]}"

                        # if --- create hr tag & continue
                        elif data[0:3] == "---":
                            in_side_li_html_data["tag"] = "hr"
                            in_side_li_html_data["content"] = ""
                        else:

                            # check if even instances of ** are present in the line
                            if data.find('*') != -1 and data.count("*") % 2 == 0:
                                ch_idxs = find(data)
                                data = sort_buld_italic(data, ch_idxs)
                            elif data.find('`') != -1 and data.count("`") % 2 == 0:
                                ch_idxs = find_back_ticks(data)
                                data = sort_buld_sm_code_block(data, ch_idxs)

                            in_side_li_html_data["tag"] = "p"
                            in_side_li_html_data["content"] = data

                        li_data["content"].append({
                            "tag": in_side_li_html_data["tag"],
                            "content": in_side_li_html_data["content"],
                        })

                    idx += 1

                # if idx < len(markdown_list):
                    # print("\n************\n\n")
                    # # print("len(markdown_list[idx].lstrip()): ", len(markdown_list[idx].lstrip()))
                    # print("len(markdown_list[idx]) - len(markdown_list[idx].lstrip()) > 0: ", len(markdown_list[idx]) - len(markdown_list[idx].lstrip()) > 0)
                    # print("\n\n************\n")

                    # print("\n************\n\n")

                    # print("markdown_list[idx]: ", f'"{markdown_list[idx]}"')
                    # print("markdown_list[idx].lstrip(): ", f'"{markdown_list[idx].lstrip()}"')
                    # print("\n")
                    # print("len(markdown_list[idx]): ", len(markdown_list[idx]))
                    # print("len(markdown_list[idx].lstrip()): ", len(markdown_list[idx].lstrip()))
                    # print("\n")
                    # print("len(markdown_list[idx]) - len(markdown_list[idx].lstrip()) > 0: ", len(markdown_list[idx]) - len(markdown_list[idx].lstrip()) > 0)

                    # print("\n\n************\n")
                
                return [idx, li_data]

            idx, li_data = make_li_tags(idx, markdown_list, depth, li_data)


            # if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
            # if_need_add_callout_line(prior_line_has_callout, how_to, html_data)
            # def is_ol_sibling(idx, markdown_list):
            #     return True if idx < len(markdown_list) and len(markdown_list[idx]) != 0 and markdown_list[idx].lstrip()[0].isnumeric() else False

            # # is_ol_sibling = markdown_list[idx].lstrip()[0].isnumeric()

            # siblying_l_type = "ol" if markdown_list[idx].lstrip()[0].isnumeric() else "ul" if markdown_list[idx].lstrip()[0] == "-" else False

            # while idx < len(markdown_list) and is_ol_main == ("ol" if markdown_list[idx].lstrip()[0].isnumeric() else "ul" if markdown_list[idx].lstrip()[0] == "-" else False):
            
            #     idx, li_data = make_li_tags(idx, markdown_list, depth, li_data)

            return [li_data, idx-1]

        idx = 0  
        # loop through markdown_list
        while idx < len(markdown_list):
            
            """
                html_data = {
                    # key: Str | List | Dict

                    # Optional ⌥
                    "bd_callout": {"indent": Int},

                    # Required❗️
                    "tag": Str,
                    # Str >>> "tag": "h2" | "h4" | "h5" | "p" | "fenced_code_block" | "code" | "strong" | "ul" | "ol" | "li" | "span" | "hr" | "em" 
                    # TODO: add to Str >>> "a" | "img" | "iframe" | "table" | "tr" | "th" | "td" | "pre" | "b" | "div" | "br" | 

                    # Required❗️ unless otherwise specified 
                    # ∞ Infinite Possible nested tags 🆘 
                    "content": Str | List | Dict
                    # "Content_Str" >>> "content": "text to display",
                    ''' [Content_List] >>> 
                    "content": [
                        # Str | [Content_List] | {Content_Dict} 
                        "text to display",
                        [ [Content_List] ],
                        {Content_Dict}
                    ],'''
                    ''' {Content_Dict} >>> 
                    "content": {
                        "tag": Str, 
                        "content": Str | [Content_List] | {Content_Dict},
                        "bd_callout": {"indent": Int} # Optional ⌥
                    },'''
                }
            """
            
            html_data = {}  

            # check if line starts with >
            html_data = bd_callout(markdown_list, idx)

            # if markdown_list[idx].lstrip() != '':
            #     idx += 1
            #     continue

            # check if code block e.g. ``` 
            if markdown_list[idx].find("```") != -1:
                # loop through the list until the next ``` is found
                idx += 1
                # make {tag: code, content: code}
                html_data["tag"] = "fenced_code_block"
                html_data["content"] = '\n'

                # loop through code_lines and add each line to the content keep indentations "space(s)" the same
                while idx < len(markdown_list) and markdown_list[idx].find("```") == -1:
                    html_data["content"] += f"{markdown_list[idx]}\n"
                    idx += 1

                # if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
                if_need_add_callout_line(prior_line_has_callout, how_to, html_data)
                
            # check if line starts with # | ## | ### followed by a space
            elif markdown_list[idx][0] == "#":
                symbol_count = 1
                if markdown_list[idx][0:2] == "##":
                    if markdown_list[idx][0:3] == "###":

                        symbol_count = 3
                        html_data["tag"] = "h5"
                    else:
                        symbol_count = 2
                        html_data["tag"] = "h4"
                else:
                    html_data["tag"] = "h2"
                
                html_data["content"] = f"{markdown_list[idx][symbol_count+1:]}"

            # if --- create hr tag & continue
            elif markdown_list[idx][0:3] == "---":
                html_data["tag"] = "hr"
                html_data["content"] = ""

            # ? Starts w/ (num >>> '.' | '-')  | space(s) >>> ( "-" | num >>> '.' )  
            elif markdown_list[idx].lstrip() != '' and (markdown_list[idx].lstrip()[0].isnumeric() and markdown_list[idx].lstrip()[1] == '.' or markdown_list[idx].lstrip()[0] == '-'):

                # get indent info
                depth = len(markdown_list[idx]) - len(markdown_list[idx].lstrip())
                
                # make html list data
                li_data, idx = make_html_list_data(html_data, markdown_list, idx, prior_line_has_callout, how_to, depth)


                html_data["tag"] = li_data["tag"]
                html_data["content"] = li_data["content"]

            # check if even instances of ** are present in the line
            elif markdown_list[idx].find('*') != -1 and markdown_list[idx].count("*") % 2 == 0:

                ch_idxs = find(markdown_list[idx])
                
                # order data acording to Md * | ** | ***
                res = sort_buld_italic(markdown_list[idx], ch_idxs)

                html_data["tag"] = res["tag"]
                html_data["content"] = res["content"]
            
            # if even instances of ` are present in the line
            elif markdown_list[idx].find('`') != -1 and markdown_list[idx].count("`") % 2 == 0:
                ch_idxs = find_back_ticks(markdown_list[idx])

                # order data acording to Md `
                data_res = sort_buld_sm_code_block(markdown_list[idx], ch_idxs)

                if data_res["tag"] == "span":
                    html_data["tag"] = "p"
                else:
                    html_data["tag"] = data_res["tag"]

                html_data["content"] = data_res["content"]
                
            
            else:
                html_data["tag"] = "p"
                html_data["content"] = markdown_list[idx]


            # if prior_line_has_callout & "bd_callout" in html_data add to last dict in how_to
            if_need_add_callout_line(prior_line_has_callout, how_to, html_data)
            # if html_data["bd_callout"] prior_line_has_callout = True
            if "bd_callout" in html_data: 
                prior_line_has_callout = True
            else:
                prior_line_has_callout = False

            how_to.append(html_data)
            idx += 1

        context["how_to"] = how_to

        return how_to

