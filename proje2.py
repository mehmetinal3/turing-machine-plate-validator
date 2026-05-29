DIGITS = set("0123456789")
LETTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

transitions = {
    ('q0', 'DIGIT'): ('q1', 'R'),
    ('q1', 'DIGIT'): ('q2', 'R'),
    ('q2', 'LETTER'): ('q3', 'R'),
    ('q3', 'LETTER'): ('q4', 'R'),
    ('q4', 'DIGIT'): ('q5', 'R'),
    ('q5', 'DIGIT'): ('q6', 'R'),
    ('q6', 'DIGIT'): ('q7', 'R'),
    ('q7', 'BLANK'): ('q_accept', 'R')
}

class TuringMachine:
    def __init__(self, input_string):
        self.tape = list(input_string) + ['_']
        self.head_position = 0
        self.current_state = 'q0'
        self.accept_state = 'q_accept'
        self.reject_state = 'q_red'
        self.is_running = True

    def step(self):
        if self.head_position < len(self.tape):
            current_char = self.tape[self.head_position]
        else:
            current_char = '_'

        if current_char in DIGITS:
            char_type = 'DIGIT'
        elif current_char in LETTERS:
            char_type = 'LETTER'
        elif current_char == '_':
            char_type = 'BLANK'
        else:
            char_type = 'INVALID'

        lookup_key = (self.current_state, char_type)
        
        tape_str = ''.join(self.tape)
        
        if lookup_key in transitions:
            new_state, movement = transitions[lookup_key]
            
            print(f"Mevcut Durum: {self.current_state: <5} | Okunan Sembol: {current_char} | Kafa Hareketi: {movement} | Bant İçeriği: {tape_str}")
            
            self.current_state = new_state
            if movement == 'R':
                self.head_position += 1
        else:
            print(f"Mevcut Durum: {self.current_state: <5} | Okunan Sembol: {current_char} -> UYUMSUZ! RED Durumuna geçiliyor.")
            self.current_state = self.reject_state
            self.is_running = False

    def run(self):
        print(f"\n--- Simülasyon Başladı ---")
        while self.is_running:
            if self.current_state == self.accept_state:
                print(f"\nSonuç: {self.current_state} -> KABUL")
                self.is_running = False
            elif self.current_state == self.reject_state:
                print(f"\nSonuç: {self.current_state} -> RED")
                self.is_running = False
            else:
                self.step()
        print(f"---------------------------\n")

if __name__ == "__main__":
    user_input = input("Lütfen kontrol edilmesini istediğiniz plakayı giriniz: ")
    
    tm = TuringMachine(user_input)
    tm.run()
