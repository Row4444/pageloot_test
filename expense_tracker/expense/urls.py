from django.urls import path
from .views import (
    ExpenseListCreateView,
    ExpenseDetailView,
    ExpenseByDateRangeView,
    CategorySummaryView,
)

urlpatterns = [
    path("expenses/", ExpenseListCreateView.as_view(), name="expense-list-create"),
    path("expenses/<int:pk>/", ExpenseDetailView.as_view(), name="expense-detail"),
    path(
        "expenses/date_range/",
        ExpenseByDateRangeView.as_view(),
        name="expense-by-date-range",
    ),
    path(
        "expenses/category_summary/",
        CategorySummaryView.as_view(),
        name="category-summary",
    ),
]
