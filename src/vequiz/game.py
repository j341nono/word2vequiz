import random
from gensim.models import KeyedVectors
from numpy import dot
from numpy.linalg import norm
import threading
import time
from vequiz.spinner import Spinner
import sys

dict_path = "src/copus/GoogleNews-vectors.bin"
model = None
model_loaded = threading.Event()

def load_model():
    global model
    try:
        model = KeyedVectors.load_word2vec_format(dict_path, binary=True)
        model_loaded.set()
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        sys.exit(1)

def get_random_k_words(model, k=2, vocab_limit=1000):
    vocab = list(model.key_to_index.keys())[:vocab_limit]
    return random.sample(vocab, k)

def get_near_words(model, words: list):
    try:
        ans_word, ans_score = model.most_similar(positive=[words[0]], negative=[words[1]], topn=1)[0]
        is_correct = (ans_word == words[2])
        if is_correct:
            user_ans_cos_sim = None  # 正解なので類似度は省略
        else:
            vec_combo = model[words[0]] + model[words[1]]
            user_ans_vec = model[words[2]]
            user_ans_cos_sim = dot(vec_combo, user_ans_vec) / (norm(vec_combo) * norm(user_ans_vec))
        return ans_word, ans_score, user_ans_cos_sim, is_correct
    except Exception as e:
        print(f"❌ Error during similarity computation: {e}")
        sys.exit(1)

def print_result(is_correct: bool, ans_word, ans_score, user_input, user_ans_cos_sim):
    print("\n==========================")
    if is_correct:
        print("✅ Great! Your answer is correct!")
    else:
        print("❌ Sorry, your answer was incorrect.")
        print(f"Your answer: {user_input}")
        print(f"→ Similarity to expected vector: {user_ans_cos_sim:.4f}")
    print("\n📌 Correct answer suggestion:")
    print(f"Answer: {ans_word}")
    print(f"→ Similarity score: {ans_score:.4f}")
    print("==========================\n")

def quiz():
    try:
        print("\n🧠 Word Vector Analogy Quiz 🧠")
        print("You will be given two words:")
        print("- One to ADD")
        print("- One to SUBTRACT")
        print("Try to guess the word closest to this vector operation:\n")
        print("        vec(A) + vec(B) ≈ ?")

        with Spinner("Loading...", "Loading... Done."):
            model_loaded.wait()

        random_words = get_random_k_words(model, 2)

        print(f"\n🔹 Word to ADD:      {random_words[0]}")
        print(f"🔸 Word to SUBTRACT: {random_words[1]}")
        print('\nWhat is the resulting word from this vector operation?\n')

        while True:
            user_input = input(">>> ").strip()
            if user_input in model.key_to_index:
                break
            print("⚠️ That word doesn't exist in the vocabulary. Please try another.")

        with Spinner("Calculating...", "Done."):
            random_words.append(user_input)
            ans_word, ans_score, user_ans_cos_sim, is_correct = get_near_words(model, random_words)
        print_result(is_correct, ans_word, ans_score, user_input, user_ans_cos_sim)

    except KeyboardInterrupt:
        print("\n🛑 Quiz interrupted by user.")
        sys.exit(0)

def main():
    model_thread = threading.Thread(target=load_model)
    model_thread.start()

    try:
        quiz()
    except KeyboardInterrupt:
        print("\n🛑 Program interrupted by user.")
        sys.exit(0)
    finally:
        model_thread.join()

if __name__ == "__main__":
    main()
