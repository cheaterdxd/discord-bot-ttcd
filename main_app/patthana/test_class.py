



# list cau hoi, cau tra loi user [[id_ques, A/B/C]]

# list câu hỏi: có câu hỏi, câu trả lời, câu trả lời đúng
# [[id_ca_hoi,A_B_C_D,A], [...]]

class user_answer:
    def __init__(self,question_id):
        self.question_id = question_id
        self.answer_A = "test1"
        self.answer_B = "test1"
        self.answer_C = "test1"
        self.answer_D = "test1"
        self.correct_answer = "D"
    question_id="" # property
    answer_user=""
    correct_answer=""
    answer_A=""
    answer_B=""
    answer_C=""
    answer_D=""
    def print_my_self(self):
        print(f"question_id: {self.question_id}, answer_user: {self.answer_user}, correct_answer: {self.correct_answer}, answer_A: {self.answer_A}, answer_B: {self.answer_B}, answer_C: {self.answer_C}, answer_D: {self.answer_D}")

# list câu hỏi
list_quest = []

# list_id_cau_hoi = get_question_id(level) 
list_id_cau_hoi = [123,124, 125]

list_user_answer = []

for i in list_id_cau_hoi:
    new_obj = user_answer(i) # khởi tạo 1 đối tượng --> instructor của class --> __init__
    # new_obj.print_my_self()


    list_user_answer.append(new_obj)
            

user_answer.question_id = "123"
# output_answer = "A"
# [user_answer,....]

save_answer(list_user_answer)


for i in list_user_answer:
    output_answer = input(f"nhâp đáp án {i.question_id}\n A. {i.answer_A}\n B. {i.answer_B}\n C. {i.answer_C}\n D. {i.answer_D}\n > ")
    i.answer_user = output_answer

# for i in list_user_answer:
#     i.print_my_self()

def check_answer(list_user_answer):
    for i in list_user_answer:
        if i.answer_user == i.correct_answer:
            print(f"Câu hỏi {i.question_id} đúng!")
        else:
            print(f"Câu hỏi {i.question_id} sai!")

check_answer(list_user_answer)