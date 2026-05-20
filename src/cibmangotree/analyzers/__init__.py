from cibmangotree.analyzer_interface import AnalyzerSuite

from .example.example_base import example_base
from .example.example_report import example_report
from .example.example_web import example_web
from .hashtags.hashtags_base import hashtags
from .hashtags.hashtags_web import hashtags_web
from .ngrams.ngrams_base import ngrams
from .ngrams.ngrams_stats import ngrams_stats
from .ngrams.ngrams_web import ngrams_web

suite = AnalyzerSuite(
    all_analyzers=[
        example_base,
        example_report,
        example_web,
        ngrams,
        ngrams_stats,
        ngrams_web,
        hashtags,
        hashtags_web,
    ]
)
