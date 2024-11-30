class CAU_HOI_TRAC_NGHIEM:
    id = 0
    quest = ""
    answer = []
    r_answer = ""
    u_answer = ""
    def __init__(self):
        pass
    def pretty_print_string(self)-> str:
        """Tạo câu hỏi dưới dạng string cho dễ in ra"""
        self_print = ""
        self_print += f"{self.quest}"
        start_prefix = 'A' 
        for i in self.answer:
            self_print += f"\n{start_prefix}. {i}"
            start_prefix = chr(ord(start_prefix) + 1)  # increment the prefix
        # self_print += f"\n{self.r_answer}"
        return self_print
    
    def parse_from_yaml(self, yaml_object):
        """
        Parse question data from a YAML object and populate the CAUHOI instance.
    
        This method takes a YAML object containing question data and assigns
        the values to the corresponding attributes of the CAUHOI instance.
    
        Parameters:
        yaml_object (dict): A dictionary containing the question data with the following keys:
            - 'ID': The unique identifier for the question
            - 'Q': The question text
            - 'A': A list of possible answers
            - 'RA': The correct answer
    
        Returns:
        None: This method modifies the instance in-place and doesn't return any value.
        """
        self.id:str = yaml_object['ID']
        self.quest:str = yaml_object["Q"]
        self.answer:list = yaml_object["A"]
        self.r_answer:str = yaml_object["RA"]

    def get_user_answer(self, user_input: str) -> int:
        """
        Validate and store the user's answer for a multiple-choice question.
    
        This method checks if the user's input is a valid answer choice (A, B, C, or D)
        for a multiple-choice question. If valid, it stores the answer in uppercase.
    
        Parameters:
        user_input (str): The user's input answer. Expected to be a single character.
    
        Returns:
        int: 0 if the input is valid (A, B, C, or D), -1 otherwise.
    
        Note:
        The method sets the instance variable 'u_answer' with the uppercase version
        of the valid input.
        """
        if len(user_input) == 1 and 'A' <= user_input.upper() <= chr(ord('A') + len(self.answer) - 1):
            self.u_answer = user_input.upper()
            return 0
        else:
            return -1
    def check_answer(self) -> bool:
        """
        Check if the user's answer matches the correct answer.

        This method compares the user's answer (stored in the 'u_answer' attribute)
        with the correct answer (stored in the 'r_answer' attribute) and returns
        True if they match, indicating that the user's answer is correct.
        Otherwise, it returns False.

        Parameters:
        None

        Returns:
        bool: True if the user's answer matches the correct answer, False otherwise.
        """
        return self.u_answer == self.r_answer


if __name__ == "__main__":
    import yaml
    q_parse = []
    with open("D:\WORKING_container\discord_bot_2\discord-bot-ttcd\main_app\patthana\cau_hoi.yaml", "r", encoding="utf-8") as f_q:
        ry_ob = yaml.full_load_all(f_q)
        for q in ry_ob: # read yaml object
            # print(q['ID'])
            a = CAU_HOI_TRAC_NGHIEM()
            a.parse_from_yaml(q)
            print(a.pretty_print_string())
            q_parse.append(a)
            u_a = str(input("answer?\n>"))
            ret = a.get_user_answer(u_a)
            while ret != 0:
                print("Invalid input. Please enter a valid answer (A, B, C, or D).")
                u_a = str(input("answer?\n>"))
                ret = a.get_user_answer(u_a)
            print(a.check_answer())


