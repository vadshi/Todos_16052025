from fastapi import APIRouter


router = APIRouter(prefix="/auth", tags=['auth'])


SECRET_KEY = '259eedaa93c111c0370f5a166cf7b3548ddf977cfd2de488bfde7fb47eea46b9'
ALGORITM = 'HS256'
