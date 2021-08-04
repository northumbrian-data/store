from typing import List, Optional
from ninja import Schema
from ninja.orm import create_schema
from pydantic import validator, typing, conint

from myauth.models import User, UserProfile, Tier, Team

TierSchema = create_schema(Tier)


class Error(Schema):
    message: str


class UserProfileIn(Schema):
    name: str
    team_id: int = None
    recovery_key: str
    invite_id: str = None
    accepted_terms_and_conditions: bool = False


class TeamSchema(Schema):
    id: int
    owner_id: int
    tier: TierSchema
    usage: int


class UserProfileOut(Schema):
    @validator("email_verified")
    def cast_verified_date_to_bool(cls, verified_date):
        return verified_date is not None

    id: int
    name: str
    email: str
    email_verified: typing.Any  # we cast this to a bool
    is_collaborator: bool
    team: TeamSchema


class InvitedProfileOut(Schema):
    email: str
    sent_date: typing.Any  # Date?!


class TeamsOut(Schema):
    profiles: List[UserProfileOut]
    pending_invites: List[InvitedProfileOut]


class CheckoutSessionIn(Schema):
    tier_id: int


class CheckoutSessionOut(Schema):
    id: str


class InviteCreated(Schema):
    id: str


class InviteOut(Schema):
    email: str
    team_id: str


class CreateInvite(Schema):
    email: str
    is_collaborator: bool = False


class AccountRecovery(Schema):
    email: str


class AccountRecoveryOut(Schema):
    recovery_key: str


class AddonIn(Schema):
    users: conint(ge=0) = 0
    projects: conint(ge=0) = 0
    collaborators: conint(ge=0) = 0


class CurrentPlanOut(Schema):
    has_billing: bool
    tier_name: str
    tier_id: int
    users_limit: Optional[conint(ge=0)] = 0
    projects_limit: Optional[conint(ge=0)] = 0
    collaborators_limit: Optional[conint(ge=0)] = 0
    users: Optional[conint(ge=0)] = 0
    projects: Optional[conint(ge=0)] = 0
    collaborators: Optional[conint(ge=0)] = 0
    storage: Optional[conint(ge=0)] = 0
