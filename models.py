"""
بناء نماذج Sequence Labeling للترقيم العربي
"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np


def build_sequence_model(model_type='lstm', vocab_size=10000, embedding_dim=100, 
                        lstm_units=128, num_classes=7, max_length=128, dropout=0.3, **params):
    """
    بناء نماذج Sequence Labeling:
    - LSTM/BiLSTM
    - GRU/BiGRU
    - Transformer-based models
    
    Args:
        model_type: نوع النموذج ('lstm', 'bilstm', 'gru', 'bigru', 'transformer')
        vocab_size: حجم المفردات
        embedding_dim: بعد التضمين
        lstm_units: عدد وحدات LSTM/GRU
        num_classes: عدد الفئات (7: بدون علامة + 6 علامات ترقيم)
        max_length: الحد الأقصى لطول التسلسل
        dropout: معدل Dropout
        **params: معاملات إضافية
    
    Returns:
        model: النموذج المبني
    """
 


def build_transfer_learning_model(pretrained_model_name='aubmindlab/bert-base-arabertv2', 
                                  num_classes=7, max_length=128, dropout=0.3):
    """
    استخدام نماذج لغوية مدربة مسبقاً (BERT-based models)
    
    Args:
        pretrained_model_name: اسم النموذج المدرب مسبقاً
        num_classes: عدد الفئات
        max_length: الحد الأقصى لطول التسلسل
        dropout: معدل Dropout
    
    Returns:
        model: النموذج المبني
        tokenizer: أداة التقطيع
    """
