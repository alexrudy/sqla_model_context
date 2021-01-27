import logging

from flask_login import current_user
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

from sqla_model_context import ModelRelativeContextManager
from sqla_model_context.exc import NoActiveRelation


log = logging.getLogger(__name__)


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)


class OwnedMixin:
    @declared_attr
    def owner_id(cls) -> Column:
        return Column(Integer, ForeignKey("users.id"))

    @declared_attr
    def owner(cls) -> relationship:
        # sqlmypy does not support declared attributes properly: https://github.com/dropbox/sqlalchemy-stubs/issues/97
        backref_name: str = cls.__tablename__  # type: ignore
        cls_name: str = cls.__name__  # type: ignore
        return relationship(
            "User", backref=backref(backref_name, lazy="dynamic", doc=f"All {cls_name}s related to this User")
        )


def _get_default_owner() -> "User":
    """Get the owner based on the context variable"""
    try:
        return current_user.user
    except AttributeError:
        pass

    raise NoActiveRelation("OwnedMixin", "user")


owner: ModelRelativeContextManager[OwnedMixin, "User"] = ModelRelativeContextManager(
    OwnedMixin, "owner", enforce="WARN", default_value=_get_default_owner
)
