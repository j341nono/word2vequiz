# word2vequiz 🧠

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An interactive word vector analogy quiz game powered by Word2Vec! Test your understanding of semantic relationships between words through vector arithmetic.

## 📝 What is word2vequiz?

word2vequiz is a command-line quiz game that challenges you to understand word relationships using vector mathematics. The game presents you with two words:
- One word to **ADD** (positive vector)
- One word to **SUBTRACT** (negative vector)

Your task is to guess which word is closest to the resulting vector operation: `vec(A) + vec(B) ≈ ?`

### Example
```
🔹 Word to ADD:      king
🔸 Word to SUBTRACT: man
>>> woman

✅ Great! Your answer is correct!
📌 Correct answer suggestion:
Answer: queen
→ Similarity score: 0.7698
```

## 🚀 Features

- **Interactive CLI Quiz**: Engaging command-line interface with emoji indicators
- **Real-time Feedback**: Immediate scoring with similarity calculations
- **Smart Validation**: Checks if your input exists in the vocabulary
- **Loading Indicators**: Beautiful spinner animations during model loading
- **Error Handling**: Robust error management for a smooth experience
- **Vector Similarity**: Shows cosine similarity scores for educational purposes

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver

Install uv first if you haven't already:
```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Quick Install (Recommended)
```bash
curl -sSL https://raw.githubusercontent.com/j341nono/word2vequiz/main/setup.sh | bash
```

### Manual Installation
```bash
# Clone the repository
git clone https://github.com/j341nono/word2vequiz.git
cd word2vequiz

# Install dependencies using uv
uv sync

# Run the setup script
./setup.sh
```

## 🎮 Usage

After installation, simply run:
```bash
vequiz
```

### Game Flow
1. The game loads the Word2Vec model (Google News vectors)
2. Two random words are selected from the vocabulary
3. You're prompted to guess the resulting word
4. The game calculates similarity and provides feedback
5. You see the correct answer with similarity scores

### Example Session
```
🧠 Word Vector Analogy Quiz 🧠
You will be given two words:
- One to ADD
- One to SUBTRACT
Try to guess the word closest to this vector operation:

        vec(A) + vec(B) ≈ ?

Loading... Done.

🔹 Word to ADD:      Paris
🔸 Word to SUBTRACT: France

What is the resulting word from this vector operation?

>>> Tokyo
Calculating... Done.

==========================
❌ Sorry, your answer was incorrect.
Your answer: Tokyo
→ Similarity to expected vector: 0.6234

📌 Correct answer suggestion:
Answer: Berlin
→ Similarity score: 0.7891
==========================
```

## 🛠️ Requirements

- Python 3.6 or higher
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver
- gensim
- numpy
- Google News Word2Vec model (automatically downloaded)

## 📊 Technical Details

- **Model**: Google News Word2Vec (3M words, 300-dimensional vectors)
- **Vocabulary**: Top 1000 most common words (configurable)
- **Similarity Metric**: Cosine similarity
- **Vector Operation**: `positive=[word1] + negative=[word2]`

## 🎯 Educational Value

This quiz helps you understand:
- **Semantic Relationships**: How words relate to each other in vector space
- **Vector Arithmetic**: Mathematical operations on word embeddings
- **Word2Vec Concepts**: Practical application of neural word embeddings
- **Natural Language Processing**: Hands-on experience with NLP techniques

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

- **Bug Reports**: Found a bug? Open an issue!
- **Feature Requests**: Have an idea? Let's discuss it!
- **Code Contributions**: Submit a pull request
- **Documentation**: Help improve the docs

### Development Setup
```bash
git clone https://github.com/j341nono/word2vequiz.git
cd word2vequiz
uv pip install -e .
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google**: For the pre-trained Word2Vec model
- **Gensim**: For the excellent Word2Vec implementation
- **Word2Vec Team**: For the groundbreaking research

## 🔗 Related Projects

- [word2vec](https://code.google.com/archive/p/word2vec/) - Original Word2Vec implementation
- [gensim](https://radimrehurek.com/gensim/) - Topic modeling and document similarity library

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Read the troubleshooting section below

### Troubleshooting

**Model loading errors:**
```bash
# Re-download the model
rm -rf src/copus/GoogleNews-vectors.bin
./setup.sh
```

**Package installation issues:**
```bash
# Upgrade uv to the latest version
uv self update

# Clear uv cache and reinstall
uv cache clean
uv pip install -r requirements.txt --refresh
```

**Permission errors:**
```bash
# Make setup script executable
chmod +x setup.sh
```

---

Made with ❤️ for NLP enthusiasts and word game lovers!