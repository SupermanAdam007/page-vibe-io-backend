class ElementInfo:
    def __init__(self, importance: int, tag: str, text: str):
        self.importance = importance
        self.tag = tag
        self.text = text

    def __repr__(self):
        return f"Score: {self.importance}; tag: {self.tag}; Text: {self.text}"
