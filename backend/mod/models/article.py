#!/usr/bin/env python3

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import re
import string

class Article(models.Model):
    """Implementation of the { Article }object model
    linked to the pre-existing User object model
    Will have a title with max_length set, description
    and eventually the body as the content of the article
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def preprocess_content(self):
        """Preprocess content for the plagiarism check"""
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def tokenize_text(self, text):
        """function to return the tokenized text"""
        return text.split()
    
    def jaccard_similarity(self, tokens1, tokens2):
        """Find common words between two texts
        Params:
            set: Groups of tokens used
            tokens: Referred texts
            union: join two items
            intersection: where words match
        Return the value of the funtion"""
        set1 = set(tokens1)
        set2 = set(tokens2)
        intersection = set.intersection(set2)
        union = set1.union(set2)
        return len(intersection) /len(union)
    
    def check_plagirarism(self):
        """function to check for identical items between texts
        If found, flag: `Plagiarism`
        Params:
            content: The items tested for
            token: broken down texts into manageable units
            article: The items written by users
            jaccard_similarity: Function to test for levels of similarity
        Returns:
            True if plagiarism is detected
        """
        new_content = self.preprocess_content(self.content)
        new_tokens = self.tokenize_text(new_content)
        all_articles = Article.objects.filter(~Q(id=self.id))
        for article in all_articles:
            existing_content = self.preprocess_content(article.content)
            existing_tokens = self.tokenize_text(existing_content)
            similarity = self.jaccard_similarity(new_tokens, existing_tokens)
            if similarity > 0.8: #If similarity exceeds this threshold, return True(Plagiarism)
                return True
            return False
        
    def save(self, *args, **kwargs):
        if self.check_plagirarism():
            raise ValueError("Plagiarism Act Detected!")
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'mod'
        ordering = ['-created_at']
    
    