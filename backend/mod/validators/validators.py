from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

class MaxImageSizeValidator:
    """Validation of image file sizes
    First going to set the maximum file size in megabytes
    Params:
        max_size: The maximum file size in megabytes
        image.size: Size of the image file uploaded
    """
    def __init__(self, max_size_mb: int) -> None:
        """Initialize a validator with maximum allowed file size in mega bytes
        Params:
            max_size_mb(int): The maximum file size allowed in megabytes
        """
        if max_size_mb < 0:
            raise ValidationError("The file size cannot be negative")
        self.max_size_mb = max_size_mb

    def validate_image_size(image):
        max_size_mb = 2
        if image.size > max_size_mb * 1024 * 1024:
            raise ValidationError(f"Image size shoould not exceed {max_size_mb}MB.")
        
    def __call__(self, value: UploadedFile) -> None:
        """does validation check
        Params:
            value (UploadedFile): The uploaded file object to validate
        Raises: 
            ValidationError: if the file size exceeds the maximum allowed size
        """
        if value.size > self.max_size_mb:
            raise ValidationError(
                ('File size cannot exceed %(max_size_mb)s bytes'),
                params={'max_size_mb': self.max_size_mb}
            )
        
    def deconstruct(self):
        """serialize the validator for Django migrations
        Returns:
            Tuple: A tuple containing the path to the class and its arguments
        """
        return ('MaxImageSizeValidator', [self.max_size_mb], {})
    

class ImageSizeValidator(MaxImageSizeValidator):
    def __init__(self, max_size_mb: int) -> None:
        super().__init__(max_size_mb)

    def __call__(self, image):
        self.validate_image_size(image)

    def validate_image_size(self, image_size):
        if image_size > self.max_size:
            raise ValidationError(f"IMage file should not exceed  {self.max_size / (1024 * 1024)}MB.")
        return super().validate_image_size()