"""
تدريب نماذج الترقيم
"""
import tensorflow as tf
from tensorflow import keras
import numpy as np
import time
from sklearn.model_selection import train_test_split


def train_punctuation_model(model, X_train, y_train, X_val, y_val, 
                           epochs=10, batch_size=32, learning_rate=0.001, 
                           use_pretrained=False, tokenizer=None, **params):
    """
    تدريب النموذج مع early stopping
    
    Args:
        model: النموذج المراد تدريبه
        X_train: بيانات التدريب
        y_train: تسميات التدريب
        X_val: بيانات التحقق
        y_val: تسميات التحقق
        epochs: عدد العصور
        batch_size: حجم الدفعة
        learning_rate: معدل التعلم
        use_pretrained: هل يستخدم نموذج مدرب مسبقاً
        tokenizer: أداة التقطيع (للنماذج المدربة مسبقاً)
        **params: معاملات إضافية
    
    Returns:
        model: النموذج المدرب
        history: تاريخ التدريب
        training_time: وقت التدريب بالثواني
    """
    

def prepare_data_for_bert(texts, labels, tokenizer, max_length=128):
    """
    تحضير البيانات للنماذج المدربة مسبقاً
    
    Args:
        texts: قائمة النصوص
        labels: التسميات
        tokenizer: أداة التقطيع
        max_length: الحد الأقصى للطول
    
    Returns:
        input_ids: معرفات المدخلات
        attention_mask: قناع الانتباه
        labels_processed: التسميات المعالجة
    """
   