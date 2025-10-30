

try:
    from sklearn.model_selection import train_test_split
    print("scikit-learn está instalda com sucesso")
except ImportError:
    print("scikit-learn não está instalada.")
