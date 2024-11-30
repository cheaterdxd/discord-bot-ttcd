class CAUHOI:
    id = 0
    quest = ""
    answer = []
    r_answer = ""
    def __init__(self):
        pass
    def pretty_print_string(self):
        self_print = ""
        self_print += f"{self.quest}"
        start_prefix = 'A' 
        for i in self.answer:
            self_print += f"\n{start_prefix}. {i}"
            start_prefix = chr(ord(start_prefix) + 1)  # increment the prefix
        # self_print += f"\n{self.r_answer}"
        return self_print
    def parse_from_yaml(self, yaml_object):
        self.id = yaml_object['ID']
        self.quest = yaml_object["Q"]
        self.answer = yaml_object["A"]
        self.r_answer = yaml_object["RA"]

if __name__ == "__main__":
    import yaml
    q_parse = []
    with open("D:\WORKING_container\discord_bot_2\discord-bot-ttcd\main_app\patthana\cau_hoi.yaml", "r", encoding="utf-8") as f_q:
        ry_ob = yaml.full_load_all(f_q)
        for q in ry_ob:
            # print(q['ID'])
            a = CAUHOI()
            a.parse_from_yaml(q)
            print(a.pretty_print_string())
            q_parse.append(a)

