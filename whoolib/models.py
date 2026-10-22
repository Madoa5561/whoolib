"""Generated model classes (do not edit by hand)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar, Dict, Optional


class Model:
    __json_keys__: ClassVar[tuple] = ()

    def to_dict(self) -> dict:
        out = {}
        for key, attr in self.__json_keys__:
            val = getattr(self, attr, None)
            if val is None:
                continue
            if isinstance(val, Model):
                val = val.to_dict()
            elif isinstance(val, list):
                val = [v.to_dict() if isinstance(v, Model) else v for v in val]
            out[key] = val
        return out

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            return data
        kwargs = {}
        for key, attr in cls.__json_keys__:
            if key in data:
                kwargs[attr] = data[key]
        return cls(**kwargs)


@dataclass
class StoredConnectedServices(Model):
    ownerWhooUserId: Any = None
    services: Any = None
    __json_keys__: ClassVar[tuple] = (('ownerWhooUserId', 'ownerWhooUserId'), ('services', 'services'))


@dataclass
class CreateUserCheckInRequest(Model):
    android: Any = None
    name: Any = None
    user_ids: Any = None
    __json_keys__: ClassVar[tuple] = (('android', 'android'), ('name', 'name'), ('user_ids', 'user_ids'))


@dataclass
class UserSpot(Model):
    id: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'),)


@dataclass
class AndroidCheckInData(Model):
    identifier: Any = None
    latitude: Any = None
    longitude: Any = None
    category: Any = None
    name: Any = None
    address: Any = None
    phone_number: Any = None
    __json_keys__: ClassVar[tuple] = (('identifier', 'identifier'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('category', 'category'), ('name', 'name'), ('address', 'address'), ('phone_number', 'phone_number'))


@dataclass
class EndStayRequestDTO(Model):
    stay_time_info: Any = None
    __json_keys__: ClassVar[tuple] = (('stay_time_info', 'stay_time_info'),)


@dataclass
class StayTimeInfo(Model):
    latitude: Any = None
    longitude: Any = None
    horizontal_accuracy: Any = None
    stayed_at: Any = None
    updated_at: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('horizontal_accuracy', 'horizontal_accuracy'), ('stayed_at', 'stayed_at'), ('updated_at', 'updated_at'))


@dataclass
class SleepWakeupRequestDTO(Model):
    user_location: Any = None
    user_battery: Any = None
    device_status: Any = None
    __json_keys__: ClassVar[tuple] = (('user_location', 'user_location'), ('user_battery', 'user_battery'), ('device_status', 'device_status'))


@dataclass
class DeviceStatus(Model):
    lock_status: Any = None
    __json_keys__: ClassVar[tuple] = (('lock_status', 'lock_status'),)


@dataclass
class UserBattery(Model):
    level: Any = None
    state: Any = None
    __json_keys__: ClassVar[tuple] = (('level', 'level'), ('state', 'state'))


@dataclass
class UserLocation(Model):
    latitude: Any = None
    longitude: Any = None
    speed: Any = None
    stayed_at: Any = None
    bearing: Any = None
    horizontal_accuracy: Any = None
    getting_location_type: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('speed', 'speed'), ('stayed_at', 'stayed_at'), ('bearing', 'bearing'), ('horizontal_accuracy', 'horizontal_accuracy'), ('getting_location_type', 'getting_location_type'))


@dataclass
class UnlockStampSheetRequest(Model):
    stamp_sheet: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_sheet', 'stamp_sheet'),)


@dataclass
class FriendCount(Model):
    friend_count: Any = None
    __json_keys__: ClassVar[tuple] = (('friend_count', 'friend_count'),)


@dataclass
class UpdateUserCheckInRequest(Model):
    android: Any = None
    name: Any = None
    user_ids: Any = None
    __json_keys__: ClassVar[tuple] = (('android', 'android'), ('name', 'name'), ('user_ids', 'user_ids'))


@dataclass
class AndroidCheckInData_UpdateUserCheckInRequest(Model):
    identifier: Any = None
    latitude: Any = None
    longitude: Any = None
    category: Any = None
    name: Any = None
    address: Any = None
    phone_number: Any = None
    __json_keys__: ClassVar[tuple] = (('identifier', 'identifier'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('category', 'category'), ('name', 'name'), ('address', 'address'), ('phone_number', 'phone_number'))


@dataclass
class UserLocationRequestDTO(Model):
    user_location: Any = None
    user_battery: Any = None
    app_state: Any = None
    user_spot: Any = None
    __json_keys__: ClassVar[tuple] = (('user_location', 'user_location'), ('user_battery', 'user_battery'), ('app_state', 'app_state'), ('user_spot', 'user_spot'))


@dataclass
class AppState(Model):
    active: Any = None
    __json_keys__: ClassVar[tuple] = (('active', 'active'),)


@dataclass
class UserBattery_UserLocationRequestDTO(Model):
    level: Any = None
    state: Any = None
    __json_keys__: ClassVar[tuple] = (('level', 'level'), ('state', 'state'))


@dataclass
class UserLocation_UserLocationRequestDTO(Model):
    latitude: Any = None
    longitude: Any = None
    speed: Any = None
    stayed_at: Any = None
    bearing: Any = None
    horizontal_accuracy: Any = None
    getting_location_type: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('speed', 'speed'), ('stayed_at', 'stayed_at'), ('bearing', 'bearing'), ('horizontal_accuracy', 'horizontal_accuracy'), ('getting_location_type', 'getting_location_type'))


@dataclass
class ReactionDTO(Model):
    id: Any = None
    image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('image_url', 'image_url'))


@dataclass
class AddReaction(Model):
    state: Any = None
    text: Any = None
    __json_keys__: ClassVar[tuple] = (('state', 'state'), ('text', 'text'))


@dataclass
class RecommendStampSheet(Model):
    stamp_sheet_id: Any = None
    priority: Any = None
    dot_image_url: Any = None
    large_ad_image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_sheet_id', 'stamp_sheet_id'), ('priority', 'priority'), ('dot_image_url', 'dot_image_url'), ('large_ad_image_url', 'large_ad_image_url'))


@dataclass
class WhatsUpReplyMessageVideoResponse(Model):
    whatsup_video: Any = None
    __json_keys__: ClassVar[tuple] = (('whatsup_video', 'whatsup_video'),)


@dataclass
class MessageDTO(Model):
    id: Any = None
    text_message: Any = None
    media_messages: Any = None
    stamp_message: Any = None
    message_type: Any = None
    event_message: Any = None
    is_reply_whatsup: Any = None
    is_whatsup_v2_reply_posted: Any = None
    uid: Any = None
    whatsup_count: Any = None
    is_watched_archived_whatsup: Any = None
    user: Any = None
    created_at: Any = None
    is_cancel: Any = None
    message_reactions: Any = None
    reply_original_message: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('text_message', 'text_message'), ('media_messages', 'media_messages'), ('stamp_message', 'stamp_message'), ('message_type', 'message_type'), ('event_message', 'event_message'), ('is_reply_whatsup', 'is_reply_whatsup'), ('is_whatsup_v2_reply_posted', 'is_whatsup_v2_reply_posted'), ('uid', 'uid'), ('whatsup_count', 'whatsup_count'), ('is_watched_archived_whatsup', 'is_watched_archived_whatsup'), ('user', 'user'), ('created_at', 'created_at'), ('is_cancel', 'is_cancel'), ('message_reactions', 'message_reactions'), ('reply_original_message', 'reply_original_message'))


@dataclass
class AddReactionText(Model):
    message_id: Any = None
    stamp_id: Any = None
    stamp_url: Any = None
    message_reaction_id: Any = None
    reaction_user_id: Any = None
    __json_keys__: ClassVar[tuple] = (('message_id', 'message_id'), ('stamp_id', 'stamp_id'), ('stamp_url', 'stamp_url'), ('message_reaction_id', 'message_reaction_id'), ('reaction_user_id', 'reaction_user_id'))


@dataclass
class WhatsUpReplyVideoDTO(Model):
    id: Any = None
    video_url: Any = None
    thumbnail_url: Any = None
    posted_slot_at: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('video_url', 'video_url'), ('thumbnail_url', 'thumbnail_url'), ('posted_slot_at', 'posted_slot_at'))


@dataclass
class EventDetailDTO(Model):
    user_id: Any = None
    display_name: Any = None
    __json_keys__: ClassVar[tuple] = (('user_id', 'user_id'), ('display_name', 'display_name'))


@dataclass
class StampSheet(Model):
    id: Any = None
    name: Any = None
    priority: Any = None
    thumbnail_image_url: Any = None
    stamps: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('name', 'name'), ('priority', 'priority'), ('thumbnail_image_url', 'thumbnail_image_url'), ('stamps', 'stamps'))


@dataclass
class EventMessageDTO(Model):
    id: Any = None
    event_type: Any = None
    detail: Any = None
    streak_info: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('event_type', 'event_type'), ('detail', 'detail'), ('streak_info', 'streak_info'))


@dataclass
class Cancel(Model):
    text: Any = None
    state: Any = None
    __json_keys__: ClassVar[tuple] = (('text', 'text'), ('state', 'state'))


@dataclass
class Stamp(Model):
    id: Any = None
    priority: Any = None
    stamp_hash: Any = None
    image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('priority', 'priority'), ('stamp_hash', 'stamp_hash'), ('image_url', 'image_url'))


@dataclass
class CancelText(Model):
    message_id: Any = None
    __json_keys__: ClassVar[tuple] = (('message_id', 'message_id'),)


@dataclass
class LinkUriInfoDTO(Model):
    uri: Any = None
    title: Any = None
    favicon: Any = None
    site_name: Any = None
    description: Any = None
    thumbnail_image: Any = None
    __json_keys__: ClassVar[tuple] = (('uri', 'uri'), ('title', 'title'), ('favicon', 'favicon'), ('site_name', 'site_name'), ('description', 'description'), ('thumbnail_image', 'thumbnail_image'))


@dataclass
class MusicChannelPayload(Model):
    event: Any = None
    user_id: Any = None
    uid: Any = None
    music: Any = None
    stopped_at: Any = None
    __json_keys__: ClassVar[tuple] = (('event', 'event'), ('user_id', 'user_id'), ('uid', 'uid'), ('music', 'music'), ('stopped_at', 'stopped_at'))


@dataclass
class Music(Model):
    site_name: Any = None
    identifier: Any = None
    title: Any = None
    artist_name: Any = None
    cover_image_url: Any = None
    service_uri: Any = None
    preview_url: Any = None
    played_at: Any = None
    played_end_at: Any = None
    expected_played_end_at: Any = None
    __json_keys__: ClassVar[tuple] = (('site_name', 'site_name'), ('identifier', 'identifier'), ('title', 'title'), ('artist_name', 'artist_name'), ('cover_image_url', 'cover_image_url'), ('service_uri', 'service_uri'), ('preview_url', 'preview_url'), ('played_at', 'played_at'), ('played_end_at', 'played_end_at'), ('expected_played_end_at', 'expected_played_end_at'))


@dataclass
class MediaMessageDTO(Model):
    id: Any = None
    media: Any = None
    send_type: Any = None
    media_type: Any = None
    thumbnail_image_url: Any = None
    media_message_watch_log: Any = None
    location: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('media', 'media'), ('send_type', 'send_type'), ('media_type', 'media_type'), ('thumbnail_image_url', 'thumbnail_image_url'), ('media_message_watch_log', 'media_message_watch_log'), ('location', 'location'))


@dataclass
class DeleteReaction(Model):
    state: Any = None
    text: Any = None
    __json_keys__: ClassVar[tuple] = (('state', 'state'), ('text', 'text'))


@dataclass
class ReactionDTO_ReactionListDTO(Model):
    id: Any = None
    priority: Any = None
    image_url: Any = None
    category: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('priority', 'priority'), ('image_url', 'image_url'), ('category', 'category'))


@dataclass
class LocationDataDTO(Model):
    latitude: Any = None
    longitude: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'))


@dataclass
class DeleteReactionText(Model):
    message_id: Any = None
    stamp_id: Any = None
    message_reaction_id: Any = None
    reaction_user_id: Any = None
    __json_keys__: ClassVar[tuple] = (('message_id', 'message_id'), ('stamp_id', 'stamp_id'), ('message_reaction_id', 'message_reaction_id'), ('reaction_user_id', 'reaction_user_id'))


@dataclass
class MediaMessageWatchLogDTO(Model):
    id: Any = None
    is_reading: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('is_reading', 'is_reading'))


@dataclass
class NewMessage(Model):
    text: Any = None
    state: Any = None
    __json_keys__: ClassVar[tuple] = (('text', 'text'), ('state', 'state'))


@dataclass
class Text(Model):
    room_id: Any = None
    unread_count: Any = None
    __json_keys__: ClassVar[tuple] = (('room_id', 'room_id'), ('unread_count', 'unread_count'))


@dataclass
class MessageReadStatusDTO(Model):
    user_id: Any = None
    opened_at: Any = None
    __json_keys__: ClassVar[tuple] = (('user_id', 'user_id'), ('opened_at', 'opened_at'))


@dataclass
class NewMessageText(Model):
    user_id: Any = None
    display_name: Any = None
    message: Any = None
    profile_image: Any = None
    __json_keys__: ClassVar[tuple] = (('user_id', 'user_id'), ('display_name', 'display_name'), ('message', 'message'), ('profile_image', 'profile_image'))


@dataclass
class StampPayload(Model):
    user: Any = None
    sender: Any = None
    stamp: Any = None
    stamp_count: Any = None
    __json_keys__: ClassVar[tuple] = (('user', 'user'), ('sender', 'sender'), ('stamp', 'stamp'), ('stamp_count', 'stamp_count'))


@dataclass
class Data(Model):
    id: Any = None
    priority: Any = None
    image_url: Any = None
    image_url_path: Any = None
    stamp_hash: Any = None
    stamp_sound: Any = None
    stamp_sheet_id: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('priority', 'priority'), ('image_url', 'image_url'), ('image_url_path', 'image_url_path'), ('stamp_hash', 'stamp_hash'), ('stamp_sound', 'stamp_sound'), ('stamp_sheet_id', 'stamp_sheet_id'))


@dataclass
class ReactionDTO_MessageDTO(Model):
    id: Any = None
    user_id: Any = None
    stamp_id: Any = None
    image_url: Any = None
    stamp_sheet_id: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('user_id', 'user_id'), ('stamp_id', 'stamp_id'), ('image_url', 'image_url'), ('stamp_sheet_id', 'stamp_sheet_id'))


@dataclass
class Read(Model):
    text: Any = None
    state: Any = None
    __json_keys__: ClassVar[tuple] = (('text', 'text'), ('state', 'state'))


@dataclass
class User(Model):
    id: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'),)


@dataclass
class ReplyOriginalMessageDTO(Model):
    id: Any = None
    text_message: Any = None
    media_messages: Any = None
    stamp_message: Any = None
    message_type: Any = None
    is_reply_whatsup: Any = None
    uid: Any = None
    user: Any = None
    is_cancel: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('text_message', 'text_message'), ('media_messages', 'media_messages'), ('stamp_message', 'stamp_message'), ('message_type', 'message_type'), ('is_reply_whatsup', 'is_reply_whatsup'), ('uid', 'uid'), ('user', 'user'), ('is_cancel', 'is_cancel'))


@dataclass
class ReadingText(Model):
    user_id: Any = None
    opened_at: Any = None
    __json_keys__: ClassVar[tuple] = (('user_id', 'user_id'), ('opened_at', 'opened_at'))


@dataclass
class ThirdPartyServiceStatus(Model):
    service_category_type: Any = None
    service_name: Any = None
    status: Any = None
    __json_keys__: ClassVar[tuple] = (('service_category_type', 'service_category_type'), ('service_name', 'service_name'), ('status', 'status'))


@dataclass
class StampMessageDTO(Model):
    id: Any = None
    stamp_sheet_id: Any = None
    image_url: Any = None
    stamp_hash: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('stamp_sheet_id', 'stamp_sheet_id'), ('image_url', 'image_url'), ('stamp_hash', 'stamp_hash'))


@dataclass
class Typing(Model):
    action: Any = None
    text: Any = None
    state: Any = None
    uid: Any = None
    __json_keys__: ClassVar[tuple] = (('action', 'action'), ('text', 'text'), ('state', 'state'), ('uid', 'uid'))


@dataclass
class UserLocationDTO(Model):
    user: Any = None
    battery: Any = None
    latitude: Any = None
    longitude: Any = None
    stayed_at: Any = None
    speed: Any = None
    sharing_type: Any = None
    updated_at: Any = None
    horizontal_accuracy: Any = None
    bearing: Any = None
    __json_keys__: ClassVar[tuple] = (('user', 'user'), ('battery', 'battery'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('stayed_at', 'stayed_at'), ('speed', 'speed'), ('sharing_type', 'sharing_type'), ('updated_at', 'updated_at'), ('horizontal_accuracy', 'horizontal_accuracy'), ('bearing', 'bearing'))


@dataclass
class StreakInfoDTO(Model):
    streak_count: Any = None
    badge: Any = None
    freeze_starts_at: Any = None
    freeze_ends_at: Any = None
    is_link_active: Any = None
    __json_keys__: ClassVar[tuple] = (('streak_count', 'streak_count'), ('badge', 'badge'), ('freeze_starts_at', 'freeze_starts_at'), ('freeze_ends_at', 'freeze_ends_at'), ('is_link_active', 'is_link_active'))


@dataclass
class BatteryDTO(Model):
    level: Any = None
    state: Any = None
    __json_keys__: ClassVar[tuple] = (('level', 'level'), ('state', 'state'))


@dataclass
class MessageReactionRequest(Model):
    message_reaction: Any = None
    __json_keys__: ClassVar[tuple] = (('message_reaction', 'message_reaction'),)


@dataclass
class TextMessageDTO(Model):
    id: Any = None
    body: Any = None
    link_uri_info_list: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('body', 'body'), ('link_uri_info_list', 'link_uri_info_list'))


@dataclass
class MessageReaction(Model):
    stamp_id: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_id', 'stamp_id'),)


@dataclass
class SpotifyConnectStateRegisterRequest(Model):
    member_type: Any = None
    device: Any = None
    __json_keys__: ClassVar[tuple] = (('member_type', 'member_type'), ('device', 'device'))


@dataclass
class Capabilities(Model):
    can_be_player: Any = None
    hidden: Any = None
    __json_keys__: ClassVar[tuple] = (('can_be_player', 'can_be_player'), ('hidden', 'hidden'))


@dataclass
class Device(Model):
    device_info: Any = None
    __json_keys__: ClassVar[tuple] = (('device_info', 'device_info'),)


@dataclass
class DeviceInfo(Model):
    capabilities: Any = None
    __json_keys__: ClassVar[tuple] = (('capabilities', 'capabilities'),)


@dataclass
class boom(Model):
    friendId: Any = None
    timestamp: Any = None
    notificationId: Any = None
    boomSummaryId: Any = None
    __json_keys__: ClassVar[tuple] = (('friendId', 'friendId'), ('timestamp', 'timestamp'), ('notificationId', 'notificationId'), ('boomSummaryId', 'boomSummaryId'))


@dataclass
class check_in_spot(Model):
    userCheckInId: Any = None
    spotName: Any = None
    latitude: Any = None
    longitude: Any = None
    timestamp: Any = None
    notificationId: Any = None
    __json_keys__: ClassVar[tuple] = (('userCheckInId', 'userCheckInId'), ('spotName', 'spotName'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('timestamp', 'timestamp'), ('notificationId', 'notificationId'))


@dataclass
class comeback(Model):
    friendId: Any = None
    timestamp: Any = None
    notificationId: Any = None
    __json_keys__: ClassVar[tuple] = (('friendId', 'friendId'), ('timestamp', 'timestamp'), ('notificationId', 'notificationId'))


@dataclass
class focus_friend_with_stamp_sheet(Model):
    friendId: Any = None
    timestamp: Any = None
    notificationId: Any = None
    __json_keys__: ClassVar[tuple] = (('friendId', 'friendId'), ('timestamp', 'timestamp'), ('notificationId', 'notificationId'))


@dataclass
class friend_check_in(Model):
    userCheckInId: Any = None
    friendCheckInId: Any = None
    timestamp: Any = None
    notificationId: Any = None
    __json_keys__: ClassVar[tuple] = (('userCheckInId', 'userCheckInId'), ('friendCheckInId', 'friendCheckInId'), ('timestamp', 'timestamp'), ('notificationId', 'notificationId'))


@dataclass
class friend_icon_change(Model):
    friendId: Any = None
    iconUrl: Any = None
    stampId: Any = None
    timestamp: Any = None
    notificationId: Any = None
    __json_keys__: ClassVar[tuple] = (('friendId', 'friendId'), ('iconUrl', 'iconUrl'), ('stampId', 'stampId'), ('timestamp', 'timestamp'), ('notificationId', 'notificationId'))


@dataclass
class place(Model):
    latitude: Any = None
    longitude: Any = None
    timestamp: Any = None
    notificationId: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('timestamp', 'timestamp'), ('notificationId', 'notificationId'))


@dataclass
class same_landmark_friend_checkin(Model):
    identifier: Any = None
    latitude: Any = None
    longitude: Any = None
    timestamp: Any = None
    notificationId: Any = None
    notificationDeliveryId: Any = None
    userId: Any = None
    __json_keys__: ClassVar[tuple] = (('identifier', 'identifier'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('timestamp', 'timestamp'), ('notificationId', 'notificationId'), ('notificationDeliveryId', 'notificationDeliveryId'), ('userId', 'userId'))


@dataclass
class short_video_timeline(Model):
    timestamp: Any = None
    notificationId: Any = None
    slotAt: Any = None
    postId: Any = None
    __json_keys__: ClassVar[tuple] = (('timestamp', 'timestamp'), ('notificationId', 'notificationId'), ('slotAt', 'slotAt'), ('postId', 'postId'))


@dataclass
class tagged_friend_checkin(Model):
    identifier: Any = None
    latitude: Any = None
    longitude: Any = None
    timestamp: Any = None
    notificationId: Any = None
    __json_keys__: ClassVar[tuple] = (('identifier', 'identifier'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('timestamp', 'timestamp'), ('notificationId', 'notificationId'))


@dataclass
class watch_log(Model):
    timestamp: Any = None
    notificationId: Any = None
    __json_keys__: ClassVar[tuple] = (('timestamp', 'timestamp'), ('notificationId', 'notificationId'))


@dataclass
class AppIconGetDialogParams(Model):
    title: Any = None
    message: Any = None
    friendsText: Any = None
    daysText: Any = None
    friendTextColor: Any = None
    dayTextColor: Any = None
    iconState: Any = None
    positiveButton: Any = None
    appIconTypeId: Any = None
    __json_keys__: ClassVar[tuple] = (('title', 'title'), ('message', 'message'), ('friendsText', 'friendsText'), ('daysText', 'daysText'), ('friendTextColor', 'friendTextColor'), ('dayTextColor', 'dayTextColor'), ('iconState', 'iconState'), ('positiveButton', 'positiveButton'), ('appIconTypeId', 'appIconTypeId'))


@dataclass
class Active(Model):
    roomId: Any = None
    friendProfileImage: Any = None
    __json_keys__: ClassVar[tuple] = (('roomId', 'roomId'), ('friendProfileImage', 'friendProfileImage'))


@dataclass
class Expired(Model):
    friendProfileImage: Any = None
    __json_keys__: ClassVar[tuple] = (('friendProfileImage', 'friendProfileImage'),)


@dataclass
class LocationPlaceCampaignDTO(Model):
    id: Any = None
    title: Any = None
    main_image_url: Any = None
    detail: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('title', 'title'), ('main_image_url', 'main_image_url'), ('detail', 'detail'))


@dataclass
class Route(Model):
    from_: Any = None
    __json_keys__: ClassVar[tuple] = (('from', 'from_'),)


@dataclass
class FriendCheckInsResponse(Model):
    friend_checkins: Any = None
    platform_location_item: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('friend_checkins', 'friend_checkins'), ('platform_location_item', 'platform_location_item'), ('next_page', 'next_page'))


@dataclass
class RecommendUserSpotDTO(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    radius_meter: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('radius_meter', 'radius_meter'))


@dataclass
class AuthInfoDTO(Model):
    email: Any = None
    auth_type: Any = None
    __json_keys__: ClassVar[tuple] = (('email', 'email'), ('auth_type', 'auth_type'))


@dataclass
class AuthorDTO(Model):
    id: Any = None
    name: Any = None
    uuid: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('name', 'name'), ('uuid', 'uuid'))


@dataclass
class UserSpotsDTO(Model):
    spots: Any = None
    __json_keys__: ClassVar[tuple] = (('spots', 'spots'),)


@dataclass
class JoinRoomDTO(Model):
    state: Any = None
    __json_keys__: ClassVar[tuple] = (('state', 'state'),)


@dataclass
class ProcessData(Model):
    pid: Any = None
    uuid: Any = None
    __json_keys__: ClassVar[tuple] = (('pid', 'pid'), ('uuid', 'uuid'))


@dataclass
class MemoryHighlightsLocationPlaceRankingEntryDTO(Model):
    rank: Any = None
    location_place: Any = None
    count: Any = None
    __json_keys__: ClassVar[tuple] = (('rank', 'rank'), ('location_place', 'location_place'), ('count', 'count'))


@dataclass
class WatchLogUser(Model):
    id: Any = None
    uid: Any = None
    display_name: Any = None
    username: Any = None
    profile_image: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('display_name', 'display_name'), ('username', 'username'), ('profile_image', 'profile_image'))


@dataclass
class PurchaseVerificationRequest(Model):
    purchase_token: Any = None
    product_id: Any = None
    __json_keys__: ClassVar[tuple] = (('purchase_token', 'purchase_token'), ('product_id', 'product_id'))


@dataclass
class FriendActionDTO(Model):
    action_type: Any = None
    user_id: Any = None
    __json_keys__: ClassVar[tuple] = (('action_type', 'action_type'), ('user_id', 'user_id'))


@dataclass
class FriendCheckInItemDTO(Model):
    user_checkin: Any = None
    user: Any = None
    __json_keys__: ClassVar[tuple] = (('user_checkin', 'user_checkin'), ('user', 'user'))


@dataclass
class RecentlyPlayedItemDTO(Model):
    music: Any = None
    user: Any = None
    __json_keys__: ClassVar[tuple] = (('music', 'music'), ('user', 'user'))


@dataclass
class UpdateWhatsUpCaptionRequest(Model):
    caption_text: Any = None
    __json_keys__: ClassVar[tuple] = (('caption_text', 'caption_text'),)


@dataclass
class SuggestUsernameRequest(Model):
    display_name: Any = None
    __json_keys__: ClassVar[tuple] = (('display_name', 'display_name'),)


@dataclass
class MessageStampListDTO(Model):
    stamp_sheets: Any = None
    recommend_stamp_sheets: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_sheets', 'stamp_sheets'), ('recommend_stamp_sheets', 'recommend_stamp_sheets'))


@dataclass
class AmazonMusicAuthState(Model):
    accessToken: Any = None
    refreshToken: Any = None
    accessTokenExpiresAt: Any = None
    customerId: Any = None
    deviceId: Any = None
    deviceType: Any = None
    musicTerritory: Any = None
    regionPrefix: Any = None
    refreshHost: Any = None
    plan: Any = None
    tier: Any = None
    role: Any = None
    linkedMemberCount: Any = None
    lastAccountTypeRecheckAt: Any = None
    ownerWhooUserId: Any = None
    __json_keys__: ClassVar[tuple] = (('accessToken', 'accessToken'), ('refreshToken', 'refreshToken'), ('accessTokenExpiresAt', 'accessTokenExpiresAt'), ('customerId', 'customerId'), ('deviceId', 'deviceId'), ('deviceType', 'deviceType'), ('musicTerritory', 'musicTerritory'), ('regionPrefix', 'regionPrefix'), ('refreshHost', 'refreshHost'), ('plan', 'plan'), ('tier', 'tier'), ('role', 'role'), ('linkedMemberCount', 'linkedMemberCount'), ('lastAccountTypeRecheckAt', 'lastAccountTypeRecheckAt'), ('ownerWhooUserId', 'ownerWhooUserId'))


@dataclass
class CheckinUserDTO(Model):
    id: Any = None
    uid: Any = None
    username: Any = None
    display_name: Any = None
    profile_image: Any = None
    spot_name: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('username', 'username'), ('display_name', 'display_name'), ('profile_image', 'profile_image'), ('spot_name', 'spot_name'))


@dataclass
class MyFootprintRateResponse(Model):
    rate_percent: Any = None
    city_polygon_name: Any = None
    __json_keys__: ClassVar[tuple] = (('rate_percent', 'rate_percent'), ('city_polygon_name', 'city_polygon_name'))


@dataclass
class PremiumUserResponse(Model):
    premium_user: Any = None
    subscription_grace_period: Any = None
    __json_keys__: ClassVar[tuple] = (('premium_user', 'premium_user'), ('subscription_grace_period', 'subscription_grace_period'))


@dataclass
class SpotifyAccessTokenResponse(Model):
    accessToken: Any = None
    accessTokenExpirationTimestampMs: Any = None
    isAnonymous: Any = None
    __json_keys__: ClassVar[tuple] = (('accessToken', 'accessToken'), ('accessTokenExpirationTimestampMs', 'accessTokenExpirationTimestampMs'), ('isAnonymous', 'isAnonymous'))


@dataclass
class BoomUserDto(Model):
    profile_image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('profile_image_url', 'profile_image_url'),)


@dataclass
class StampMessageUserDTO(Model):
    id: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'),)


@dataclass
class User_MessageEntity(Model):
    id: Any = None
    uid: Any = None
    displayName: Any = None
    profileImageUrl: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('displayName', 'displayName'), ('profileImageUrl', 'profileImageUrl'))


@dataclass
class WhatsUpDTO(Model):
    id: Any = None
    video_url: Any = None
    posted_slot_at: Any = None
    latitude: Any = None
    longitude: Any = None
    created_at: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('video_url', 'video_url'), ('posted_slot_at', 'posted_slot_at'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('created_at', 'created_at'))


@dataclass
class WhatsUpReactorsResponse(Model):
    reaction_stamps: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('reaction_stamps', 'reaction_stamps'), ('next_page', 'next_page'))


@dataclass
class LocationPlaceCampaignDetailDTO(Model):
    description: Any = None
    external_url: Any = None
    __json_keys__: ClassVar[tuple] = (('description', 'description'), ('external_url', 'external_url'))


@dataclass
class WhatsUpWithUserDTO(Model):
    id: Any = None
    video_url: Any = None
    thumbnail_url: Any = None
    posted_slot_at: Any = None
    latitude: Any = None
    longitude: Any = None
    created_at: Any = None
    user: Any = None
    caption_text: Any = None
    reaction_summaries: Any = None
    my_reaction: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('video_url', 'video_url'), ('thumbnail_url', 'thumbnail_url'), ('posted_slot_at', 'posted_slot_at'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('created_at', 'created_at'), ('user', 'user'), ('caption_text', 'caption_text'), ('reaction_summaries', 'reaction_summaries'), ('my_reaction', 'my_reaction'))


@dataclass
class RecommendUserSpotRequest(Model):
    spot_type: Any = None
    latitude: Any = None
    longitude: Any = None
    __json_keys__: ClassVar[tuple] = (('spot_type', 'spot_type'), ('latitude', 'latitude'), ('longitude', 'longitude'))


@dataclass
class ActivateThirdPartyServicesRequest(Model):
    service_name: Any = None
    __json_keys__: ClassVar[tuple] = (('service_name', 'service_name'),)


@dataclass
class ErrorsDTO(Model):
    error_code: Any = None
    errors: Any = None
    __json_keys__: ClassVar[tuple] = (('error_code', 'error_code'), ('errors', 'errors'))


@dataclass
class UserCheckInSpotsResponse(Model):
    user_checkins: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('user_checkins', 'user_checkins'), ('next_page', 'next_page'))


@dataclass
class ShouldSuggestSpotResponse(Model):
    should_suggest: Any = None
    __json_keys__: ClassVar[tuple] = (('should_suggest', 'should_suggest'),)


@dataclass
class BannerAutoRefreshConfig(Model):
    enabled: Any = None
    interval: Any = None
    __json_keys__: ClassVar[tuple] = (('enabled', 'enabled'), ('interval', 'interval'))


@dataclass
class RoomUserDTO(Model):
    id: Any = None
    username: Any = None
    display_name: Any = None
    profile_image: Any = None
    friendship: Any = None
    join_room: Any = None
    friend_count: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('username', 'username'), ('display_name', 'display_name'), ('profile_image', 'profile_image'), ('friendship', 'friendship'), ('join_room', 'join_room'), ('friend_count', 'friend_count'))


@dataclass
class MemoryHighlightsLocationPlacesRankingResponseDTO(Model):
    month: Any = None
    ranking: Any = None
    __json_keys__: ClassVar[tuple] = (('month', 'month'), ('ranking', 'ranking'))


@dataclass
class Detail(Model):
    userId: Any = None
    displayName: Any = None
    __json_keys__: ClassVar[tuple] = (('userId', 'userId'), ('displayName', 'displayName'))


@dataclass
class NowPlayingMusicResponse(Model):
    user_ids: Any = None
    __json_keys__: ClassVar[tuple] = (('user_ids', 'user_ids'),)


@dataclass
class RawLocationRecord(Model):
    latitude: Any = None
    longitude: Any = None
    horizontalAccuracy: Any = None
    altitude: Any = None
    velocity: Any = None
    bearing: Any = None
    time: Any = None
    state: Any = None
    isForeground: Any = None
    charging: Any = None
    batteryLevel: Any = None
    expired: Any = None
    valid: Any = None
    provider: Any = None
    isWifiConnected: Any = None
    enablePost: Any = None
    significantMotionTriggered: Any = None
    hasSpeed: Any = None
    hasSpeedAccuracy: Any = None
    speedAccuracyMetersPerSecond: Any = None
    isJumped: Any = None
    locationModelVariant: Any = None
    jumpScore: Any = None
    consecutiveJumpCount: Any = None
    jumpInputDistance: Any = None
    stayedAt: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('horizontalAccuracy', 'horizontalAccuracy'), ('altitude', 'altitude'), ('velocity', 'velocity'), ('bearing', 'bearing'), ('time', 'time'), ('state', 'state'), ('isForeground', 'isForeground'), ('charging', 'charging'), ('batteryLevel', 'batteryLevel'), ('expired', 'expired'), ('valid', 'valid'), ('provider', 'provider'), ('isWifiConnected', 'isWifiConnected'), ('enablePost', 'enablePost'), ('significantMotionTriggered', 'significantMotionTriggered'), ('hasSpeed', 'hasSpeed'), ('hasSpeedAccuracy', 'hasSpeedAccuracy'), ('speedAccuracyMetersPerSecond', 'speedAccuracyMetersPerSecond'), ('isJumped', 'isJumped'), ('locationModelVariant', 'locationModelVariant'), ('jumpScore', 'jumpScore'), ('consecutiveJumpCount', 'consecutiveJumpCount'), ('jumpInputDistance', 'jumpInputDistance'), ('stayedAt', 'stayedAt'))


@dataclass
class LocationSharingBody(Model):
    sharing_type: Any = None
    friend_ids: Any = None
    durations: Any = None
    __json_keys__: ClassVar[tuple] = (('sharing_type', 'sharing_type'), ('friend_ids', 'friend_ids'), ('durations', 'durations'))


@dataclass
class Route_FriendAppealIconCropScreen(Model):
    image: Any = None
    __json_keys__: ClassVar[tuple] = (('image', 'image'),)


@dataclass
class UploadFootprintUrlDTO(Model):
    url: Any = None
    __json_keys__: ClassVar[tuple] = (('url', 'url'),)


@dataclass
class SuggestUsernameResponse(Model):
    username: Any = None
    __json_keys__: ClassVar[tuple] = (('username', 'username'),)


@dataclass
class CheckinUsersRequest(Model):
    os_info: Any = None
    identifiers: Any = None
    __json_keys__: ClassVar[tuple] = (('os_info', 'os_info'), ('identifiers', 'identifiers'))


@dataclass
class MyIconRingResponse(Model):
    icon_ring_type: Any = None
    __json_keys__: ClassVar[tuple] = (('icon_ring_type', 'icon_ring_type'),)


@dataclass
class NearbyUserDTO(Model):
    id: Any = None
    uid: Any = None
    username: Any = None
    display_name: Any = None
    profile_image: Any = None
    introduction: Any = None
    online: Any = None
    private_mode: Any = None
    your_world_disclosure_scope: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('username', 'username'), ('display_name', 'display_name'), ('profile_image', 'profile_image'), ('introduction', 'introduction'), ('online', 'online'), ('private_mode', 'private_mode'), ('your_world_disclosure_scope', 'your_world_disclosure_scope'))


@dataclass
class StampMessagesDTO(Model):
    stamp_messages: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_messages', 'stamp_messages'),)


@dataclass
class LocationPlaceCampaignsResponse(Model):
    campaigns: Any = None
    landmark_image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('campaigns', 'campaigns'), ('landmark_image_url', 'landmark_image_url'))


@dataclass
class ReactionListDTO(Model):
    stamps: Any = None
    __json_keys__: ClassVar[tuple] = (('stamps', 'stamps'),)


@dataclass
class User_response(Model):
    id: Any = None
    display_name: Any = None
    username: Any = None
    profile_image: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('display_name', 'display_name'), ('username', 'username'), ('profile_image', 'profile_image'))


@dataclass
class user_checkin(Model):
    id: Any = None
    spot_name: Any = None
    latitude: Any = None
    longitude: Any = None
    spot_category: Any = None
    checkin_count: Any = None
    stay_checkin_count: Any = None
    is_myspot_recommend: Any = None
    user_spot: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('spot_name', 'spot_name'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_category', 'spot_category'), ('checkin_count', 'checkin_count'), ('stay_checkin_count', 'stay_checkin_count'), ('is_myspot_recommend', 'is_myspot_recommend'), ('user_spot', 'user_spot'))


@dataclass
class UserCheckInsResponse(Model):
    user_checkins: Any = None
    __json_keys__: ClassVar[tuple] = (('user_checkins', 'user_checkins'),)


@dataclass
class PlatformLocationItemDTO(Model):
    platform_type: Any = None
    identifier: Any = None
    name: Any = None
    __json_keys__: ClassVar[tuple] = (('platform_type', 'platform_type'), ('identifier', 'identifier'), ('name', 'name'))


@dataclass
class VersionControlDTO(Model):
    minimum_support_version: Any = None
    recommend_version: Any = None
    update_url: Any = None
    __json_keys__: ClassVar[tuple] = (('minimum_support_version', 'minimum_support_version'), ('recommend_version', 'recommend_version'), ('update_url', 'update_url'))


@dataclass
class PremiumUserSetting(Model):
    app_ui_color: Any = None
    __json_keys__: ClassVar[tuple] = (('app_ui_color', 'app_ui_color'),)


@dataclass
class MemoryHighlightsTimeWithUsersEntryDTO(Model):
    rank: Any = None
    user: Any = None
    time_with_hours: Any = None
    __json_keys__: ClassVar[tuple] = (('rank', 'rank'), ('user', 'user'), ('time_with_hours', 'time_with_hours'))


@dataclass
class FootprintDownloadStatusResponse(Model):
    required_refresh: Any = None
    __json_keys__: ClassVar[tuple] = (('required_refresh', 'required_refresh'),)


@dataclass
class FootprintRateWorldRankingResponse(Model):
    footprint_rates: Any = None
    city_polygon_name: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('footprint_rates', 'footprint_rates'), ('city_polygon_name', 'city_polygon_name'), ('next_page', 'next_page'))


@dataclass
class EventMessage(Model):
    id: Any = None
    users: Any = None
    eventType: Any = None
    streakInfo: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('users', 'users'), ('eventType', 'eventType'), ('streakInfo', 'streakInfo'))


@dataclass
class WhatsUpReminderConfigDTO(Model):
    enabled: Any = None
    start_hour: Any = None
    end_hour: Any = None
    __json_keys__: ClassVar[tuple] = (('enabled', 'enabled'), ('start_hour', 'start_hour'), ('end_hour', 'end_hour'))


@dataclass
class WhatsUpStatusErrorResponse(Model):
    code: Any = None
    __json_keys__: ClassVar[tuple] = (('code', 'code'),)


@dataclass
class LocationSharingDTO(Model):
    sharing_type: Any = None
    __json_keys__: ClassVar[tuple] = (('sharing_type', 'sharing_type'),)


@dataclass
class UploadMediaUrlDTO(Model):
    urls: Any = None
    __json_keys__: ClassVar[tuple] = (('urls', 'urls'),)


@dataclass
class FriendDTO(Model):
    friend: Any = None
    __json_keys__: ClassVar[tuple] = (('friend', 'friend'),)


@dataclass
class CampaignBannerResponse(Model):
    location_place: Any = None
    banner_info: Any = None
    __json_keys__: ClassVar[tuple] = (('location_place', 'location_place'), ('banner_info', 'banner_info'))


@dataclass
class ActivityLogRequest(Model):
    global_uuid: Any = None
    session_uuid: Any = None
    session_type: Any = None
    step: Any = None
    timestamp: Any = None
    __json_keys__: ClassVar[tuple] = (('global_uuid', 'global_uuid'), ('session_uuid', 'session_uuid'), ('session_type', 'session_type'), ('step', 'step'), ('timestamp', 'timestamp'))


@dataclass
class GeocodeCenterDTO(Model):
    latitude: Any = None
    longitude: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'))


@dataclass
class PinnedRoomRequestBody(Model):
    room_id: Any = None
    __json_keys__: ClassVar[tuple] = (('room_id', 'room_id'),)


@dataclass
class CheckinUsersResponse(Model):
    checkined_users: Any = None
    __json_keys__: ClassVar[tuple] = (('checkined_users', 'checkined_users'),)


@dataclass
class ThirdPartyServiceStatusDTO(Model):
    status: Any = None
    service_name: Any = None
    __json_keys__: ClassVar[tuple] = (('status', 'status'), ('service_name', 'service_name'))


@dataclass
class RoomUsersResponse(Model):
    users: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('users', 'users'), ('next_page', 'next_page'))


@dataclass
class BoomFriendLocationsResponse(Model):
    boom_users: Any = None
    gathering: Any = None
    location: Any = None
    __json_keys__: ClassVar[tuple] = (('boom_users', 'boom_users'), ('gathering', 'gathering'), ('location', 'location'))


@dataclass
class CompletionOriginalStampRoute(Model):
    capturedFiles: Any = None
    from_: Any = None
    __json_keys__: ClassVar[tuple] = (('capturedFiles', 'capturedFiles'), ('from', 'from_'))


@dataclass
class LocationPlaceDTO(Model):
    id: Any = None
    uid: Any = None
    name: Any = None
    latitude: Any = None
    longitude: Any = None
    identifier: Any = None
    category: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('name', 'name'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('identifier', 'identifier'), ('category', 'category'))


@dataclass
class FriendCheckInLocationDTO(Model):
    identifier: Any = None
    latitude: Any = None
    longitude: Any = None
    category: Any = None
    name: Any = None
    __json_keys__: ClassVar[tuple] = (('identifier', 'identifier'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('category', 'category'), ('name', 'name'))


@dataclass
class FriendsDTO(Model):
    friends: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('friends', 'friends'), ('next_page', 'next_page'))


@dataclass
class UserAccount(Model):
    display_name: Any = None
    profile_image: Any = None
    birthday: Any = None
    username: Any = None
    email: Any = None
    password: Any = None
    referrership_uid: Any = None
    adid: Any = None
    __json_keys__: ClassVar[tuple] = (('display_name', 'display_name'), ('profile_image', 'profile_image'), ('birthday', 'birthday'), ('username', 'username'), ('email', 'email'), ('password', 'password'), ('referrership_uid', 'referrership_uid'), ('adid', 'adid'))


@dataclass
class PlatformLocationItemResponse(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    spot_category: Any = None
    spot_name: Any = None
    platform_location_item: Any = None
    tagged_users: Any = None
    last_stayed_at: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_category', 'spot_category'), ('spot_name', 'spot_name'), ('platform_location_item', 'platform_location_item'), ('tagged_users', 'tagged_users'), ('last_stayed_at', 'last_stayed_at'))


@dataclass
class BannerInfoDTO(Model):
    display_flg: Any = None
    display_seconds: Any = None
    url: Any = None
    text: Any = None
    __json_keys__: ClassVar[tuple] = (('display_flg', 'display_flg'), ('display_seconds', 'display_seconds'), ('url', 'url'), ('text', 'text'))


@dataclass
class PremiumUserSettingsRequest(Model):
    premium_user_setting: Any = None
    __json_keys__: ClassVar[tuple] = (('premium_user_setting', 'premium_user_setting'),)


@dataclass
class MediaUploadRequest(Model):
    media: Any = None
    __json_keys__: ClassVar[tuple] = (('media', 'media'),)


@dataclass
class MemoryHighlightsTimeWithUsersRankingResponseDTO(Model):
    month: Any = None
    ranking: Any = None
    __json_keys__: ClassVar[tuple] = (('month', 'month'), ('ranking', 'ranking'))


@dataclass
class BumpResponse(Model):
    users: Any = None
    __json_keys__: ClassVar[tuple] = (('users', 'users'),)


@dataclass
class LinkUriInfo(Model):
    uri: Any = None
    title: Any = None
    favicon: Any = None
    siteName: Any = None
    description: Any = None
    thumbnailImage: Any = None
    __json_keys__: ClassVar[tuple] = (('uri', 'uri'), ('title', 'title'), ('favicon', 'favicon'), ('siteName', 'siteName'), ('description', 'description'), ('thumbnailImage', 'thumbnailImage'))


@dataclass
class WhatsUpStatusResponse(Model):
    slot_at: Any = None
    status: Any = None
    __json_keys__: ClassVar[tuple] = (('slot_at', 'slot_at'), ('status', 'status'))


@dataclass
class CreateSupportTicketRequest(Model):
    category: Any = None
    body: Any = None
    subject: Any = None
    client_context: Any = None
    fcm_token: Any = None
    __json_keys__: ClassVar[tuple] = (('category', 'category'), ('body', 'body'), ('subject', 'subject'), ('client_context', 'client_context'), ('fcm_token', 'fcm_token'))


@dataclass
class SettingBannerResponse(Model):
    banner_type: Any = None
    banner_image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('banner_type', 'banner_type'), ('banner_image_url', 'banner_image_url'))


@dataclass
class UploadOriginalStampsUrlResponse(Model):
    url: Any = None
    path: Any = None
    __json_keys__: ClassVar[tuple] = (('url', 'url'), ('path', 'path'))


@dataclass
class FriendDetailDTO(Model):
    friend: Any = None
    errors: Any = None
    __json_keys__: ClassVar[tuple] = (('friend', 'friend'), ('errors', 'errors'))


@dataclass
class UserCheckInDetailResponse(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    spot_category: Any = None
    spot_name: Any = None
    address: Any = None
    stayed_at: Any = None
    left_at: Any = None
    stay_time_minute: Any = None
    notify_identifier: Any = None
    platform_location_item: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_category', 'spot_category'), ('spot_name', 'spot_name'), ('address', 'address'), ('stayed_at', 'stayed_at'), ('left_at', 'left_at'), ('stay_time_minute', 'stay_time_minute'), ('notify_identifier', 'notify_identifier'), ('platform_location_item', 'platform_location_item'))


@dataclass
class SupportTicketDTO(Model):
    id: Any = None
    category: Any = None
    subject: Any = None
    status: Any = None
    unread_by_user: Any = None
    last_activity_at: Any = None
    created_at: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('category', 'category'), ('subject', 'subject'), ('status', 'status'), ('unread_by_user', 'unread_by_user'), ('last_activity_at', 'last_activity_at'), ('created_at', 'created_at'))


@dataclass
class GeocodeDTO(Model):
    country_name: Any = None
    city_polygon_uuid: Any = None
    polygon_url: Any = None
    city_polygon_name: Any = None
    admin_level: Any = None
    center: Any = None
    __json_keys__: ClassVar[tuple] = (('country_name', 'country_name'), ('city_polygon_uuid', 'city_polygon_uuid'), ('polygon_url', 'polygon_url'), ('city_polygon_name', 'city_polygon_name'), ('admin_level', 'admin_level'), ('center', 'center'))


@dataclass
class CheckinedUserDTO(Model):
    identifier: Any = None
    checkin_users: Any = None
    __json_keys__: ClassVar[tuple] = (('identifier', 'identifier'), ('checkin_users', 'checkin_users'))


@dataclass
class RoomInvitationDTO(Model):
    id: Any = None
    uid: Any = None
    name: Any = None
    icon_image: Any = None
    state: Any = None
    join_room_state: Any = None
    users: Any = None
    inviter_user: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('name', 'name'), ('icon_image', 'icon_image'), ('state', 'state'), ('join_room_state', 'join_room_state'), ('users', 'users'), ('inviter_user', 'inviter_user'))


@dataclass
class RoomRequestBody(Model):
    room: Any = None
    __json_keys__: ClassVar[tuple] = (('room', 'room'),)


@dataclass
class RoomWhatsupBody(Model):
    message: Any = None
    __json_keys__: ClassVar[tuple] = (('message', 'message'),)


@dataclass
class SpotifyApresolveResponse(Model):
    dealer_g2: Any = None
    spclient: Any = None
    __json_keys__: ClassVar[tuple] = (('dealer-g2', 'dealer_g2'), ('spclient', 'spclient'))


@dataclass
class LegacyRecommendAdDTO(Model):
    stamp_sheet_id: Any = None
    priority: Any = None
    dot_image_url: Any = None
    large_ad_image_url: Any = None
    is_once_bring_front: Any = None
    once_bring_front_cache_key: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_sheet_id', 'stamp_sheet_id'), ('priority', 'priority'), ('dot_image_url', 'dot_image_url'), ('large_ad_image_url', 'large_ad_image_url'), ('is_once_bring_front', 'is_once_bring_front'), ('once_bring_front_cache_key', 'once_bring_front_cache_key'))


@dataclass
class FootprintRateDTO(Model):
    user: Any = None
    rate_percent: Any = None
    __json_keys__: ClassVar[tuple] = (('user', 'user'), ('rate_percent', 'rate_percent'))


@dataclass
class NearbyUsersDiscoveryRequest(Model):
    latitude: Any = None
    longitude: Any = None
    unix_timestamp: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('unix_timestamp', 'unix_timestamp'))


@dataclass
class WhatsUpMixedVideoExistsResponse(Model):
    exists: Any = None
    __json_keys__: ClassVar[tuple] = (('exists', 'exists'),)


@dataclass
class AuthInfoEditRoute(Model):
    title: Any = None
    ordinal: Any = None
    oldPassword: Any = None
    __json_keys__: ClassVar[tuple] = (('title', 'title'), ('ordinal', 'ordinal'), ('oldPassword', 'oldPassword'))


@dataclass
class FriendsIconRingItem(Model):
    icon_ring_type: Any = None
    granted_user_ids: Any = None
    __json_keys__: ClassVar[tuple] = (('icon_ring_type', 'icon_ring_type'), ('granted_user_ids', 'granted_user_ids'))


@dataclass
class CampaignLocationPlaceDTO(Model):
    id: Any = None
    uid: Any = None
    name: Any = None
    latitude: Any = None
    longitude: Any = None
    identifier: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('name', 'name'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('identifier', 'identifier'))


@dataclass
class MessagesDTO(Model):
    messages: Any = None
    next_page: Any = None
    room: Any = None
    __json_keys__: ClassVar[tuple] = (('messages', 'messages'), ('next_page', 'next_page'), ('room', 'room'))


@dataclass
class UserDTO(Model):
    id: Any = None
    uid: Any = None
    username: Any = None
    display_name: Any = None
    footprint_uuid: Any = None
    profile_image: Any = None
    introduction: Any = None
    online: Any = None
    login_days: Any = None
    max_login_days: Any = None
    created_at: Any = None
    block_information: Any = None
    friendship: Any = None
    watch_count: Any = None
    watch_user_count: Any = None
    pop_points: Any = None
    friend_count: Any = None
    time_with: Any = None
    birthday: Any = None
    your_world_disclosure_scope: Any = None
    private_mode: Any = None
    allow_recommended_users: Any = None
    user_app_icons: Any = None
    location: Any = None
    world_rank: Any = None
    user_type: Any = None
    whoo_supporter: Any = None
    location_sharing: Any = None
    whatsup_count: Any = None
    bump_count: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('username', 'username'), ('display_name', 'display_name'), ('footprint_uuid', 'footprint_uuid'), ('profile_image', 'profile_image'), ('introduction', 'introduction'), ('online', 'online'), ('login_days', 'login_days'), ('max_login_days', 'max_login_days'), ('created_at', 'created_at'), ('block_information', 'block_information'), ('friendship', 'friendship'), ('watch_count', 'watch_count'), ('watch_user_count', 'watch_user_count'), ('pop_points', 'pop_points'), ('friend_count', 'friend_count'), ('time_with', 'time_with'), ('birthday', 'birthday'), ('your_world_disclosure_scope', 'your_world_disclosure_scope'), ('private_mode', 'private_mode'), ('allow_recommended_users', 'allow_recommended_users'), ('user_app_icons', 'user_app_icons'), ('location', 'location'), ('world_rank', 'world_rank'), ('user_type', 'user_type'), ('whoo_supporter', 'whoo_supporter'), ('location_sharing', 'location_sharing'), ('whatsup_count', 'whatsup_count'), ('bump_count', 'bump_count'))


@dataclass
class RegisteredSpotResponse(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    spot_category: Any = None
    spot_name: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_category', 'spot_category'), ('spot_name', 'spot_name'))


@dataclass
class ThirdPartyServicesIntegrationStatusResponse(Model):
    thirdparty_services: Any = None
    __json_keys__: ClassVar[tuple] = (('thirdparty_services', 'thirdparty_services'),)


@dataclass
class Route_DeleteOriginalStampScreen(Model):
    stampId: Any = None
    stampUrl: Any = None
    __json_keys__: ClassVar[tuple] = (('stampId', 'stampId'), ('stampUrl', 'stampUrl'))


@dataclass
class MemoryHighlightsUserDTO(Model):
    id: Any = None
    uid: Any = None
    display_name: Any = None
    username: Any = None
    profile_image: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('display_name', 'display_name'), ('username', 'username'), ('profile_image', 'profile_image'))


@dataclass
class StampSheetDTO(Model):
    id: Any = None
    name: Any = None
    priority: Any = None
    is_display_whatsup: Any = None
    stamps: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('name', 'name'), ('priority', 'priority'), ('is_display_whatsup', 'is_display_whatsup'), ('stamps', 'stamps'))


@dataclass
class AppIconChangeRoute(Model):
    iconType: Any = None
    __json_keys__: ClassVar[tuple] = (('iconType', 'iconType'),)


@dataclass
class Location(Model):
    latitude: Any = None
    longitude: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'))


@dataclass
class StampSheetsDTO(Model):
    stamp_sheets: Any = None
    recommend_stamp_sheets: Any = None
    unlock_friend_count_conditions: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_sheets', 'stamp_sheets'), ('recommend_stamp_sheets', 'recommend_stamp_sheets'), ('unlock_friend_count_conditions', 'unlock_friend_count_conditions'))


@dataclass
class Route_QrScreen(Model):
    screenMode: Any = None
    from_: Any = None
    __json_keys__: ClassVar[tuple] = (('screenMode', 'screenMode'), ('from', 'from_'))


@dataclass
class Location_request(Model):
    latLng: Any = None
    __json_keys__: ClassVar[tuple] = (('latLng', 'latLng'),)


@dataclass
class WhatsUpRequestPostErrorResponse(Model):
    code: Any = None
    __json_keys__: ClassVar[tuple] = (('code', 'code'),)


@dataclass
class LocationPlaceMediaItemDTO(Model):
    id: Any = None
    url: Any = None
    description: Any = None
    priority: Any = None
    thumbnail_image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('url', 'url'), ('description', 'description'), ('priority', 'priority'), ('thumbnail_image_url', 'thumbnail_image_url'))


@dataclass
class FriendCheckInResponse(Model):
    users: Any = None
    checkin: Any = None
    android: Any = None
    __json_keys__: ClassVar[tuple] = (('users', 'users'), ('checkin', 'checkin'), ('android', 'android'))


@dataclass
class UploadProfileImageUrlDTO(Model):
    original: Any = None
    thumbnail: Any = None
    __json_keys__: ClassVar[tuple] = (('original', 'original'), ('thumbnail', 'thumbnail'))


@dataclass
class SubscriptionGracePeriodBody(Model):
    expires_at: Any = None
    show_modal: Any = None
    modal_type: Any = None
    __json_keys__: ClassVar[tuple] = (('expires_at', 'expires_at'), ('show_modal', 'show_modal'), ('modal_type', 'modal_type'))


@dataclass
class SupportClientContext(Model):
    app_version: Any = None
    os_version: Any = None
    device_model: Any = None
    locale: Any = None
    __json_keys__: ClassVar[tuple] = (('app_version', 'app_version'), ('os_version', 'os_version'), ('device_model', 'device_model'), ('locale', 'locale'))


@dataclass
class SupportTicketResponse(Model):
    ticket: Any = None
    __json_keys__: ClassVar[tuple] = (('ticket', 'ticket'),)


@dataclass
class UserNavArg(Model):
    id: Any = None
    displayName: Any = None
    profileImage: Any = None
    location: Any = None
    friendship: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('displayName', 'displayName'), ('profileImage', 'profileImage'), ('location', 'location'), ('friendship', 'friendship'))


@dataclass
class ChangeProfileImageRequest(Model):
    profile_image: Any = None
    is_appeal_friends: Any = None
    __json_keys__: ClassVar[tuple] = (('profile_image', 'profile_image'), ('is_appeal_friends', 'is_appeal_friends'))


@dataclass
class MarkedCheckInCheckinUserDTO(Model):
    profile_image: Any = None
    __json_keys__: ClassVar[tuple] = (('profile_image', 'profile_image'),)


@dataclass
class RoomInvitationResponse(Model):
    room: Any = None
    inviter_user: Any = None
    error_code: Any = None
    room_id: Any = None
    __json_keys__: ClassVar[tuple] = (('room', 'room'), ('inviter_user', 'inviter_user'), ('error_code', 'error_code'), ('room_id', 'room_id'))


@dataclass
class RoomRequestBodyFields(Model):
    name: Any = None
    icon_image: Any = None
    add_user_ids: Any = None
    remove_user_ids: Any = None
    uid: Any = None
    __json_keys__: ClassVar[tuple] = (('name', 'name'), ('icon_image', 'icon_image'), ('add_user_ids', 'add_user_ids'), ('remove_user_ids', 'remove_user_ids'), ('uid', 'uid'))


@dataclass
class PresignedUrlResponse(Model):
    url: Any = None
    path: Any = None
    __json_keys__: ClassVar[tuple] = (('url', 'url'), ('path', 'path'))


@dataclass
class RoomWhatsupBodyData(Model):
    uid: Any = None
    __json_keys__: ClassVar[tuple] = (('uid', 'uid'),)


@dataclass
class NearbyUsersDiscoveryResponse(Model):
    friends: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('friends', 'friends'), ('next_page', 'next_page'))


@dataclass
class WhatsUpMyReactionDTO(Model):
    stamp: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp', 'stamp'),)


@dataclass
class WhatsUpTimelineResponse(Model):
    whatsup_videos: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('whatsup_videos', 'whatsup_videos'), ('next_page', 'next_page'))


@dataclass
class CreateWhatsUpRequest(Model):
    video_path: Any = None
    thumbnail_path: Any = None
    latitude: Any = None
    longitude: Any = None
    caption_text: Any = None
    __json_keys__: ClassVar[tuple] = (('video_path', 'video_path'), ('thumbnail_path', 'thumbnail_path'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('caption_text', 'caption_text'))


@dataclass
class RecommendUserSpotsResponse(Model):
    recommend_user_spots: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('recommend_user_spots', 'recommend_user_spots'), ('next_page', 'next_page'))


@dataclass
class FriendsIconRingsResponse(Model):
    icon_rings: Any = None
    __json_keys__: ClassVar[tuple] = (('icon_rings', 'icon_rings'),)


@dataclass
class UserDetailDTO(Model):
    friends: Any = None
    user: Any = None
    next_page: Any = None
    mutual_total_count: Any = None
    total_count: Any = None
    __json_keys__: ClassVar[tuple] = (('friends', 'friends'), ('user', 'user'), ('next_page', 'next_page'), ('mutual_total_count', 'mutual_total_count'), ('total_count', 'total_count'))


@dataclass
class SavedTrack(Model):
    asin: Any = None
    isPaused: Any = None
    durationSec: Any = None
    sentAtEpochMs: Any = None
    __json_keys__: ClassVar[tuple] = (('asin', 'asin'), ('isPaused', 'isPaused'), ('durationSec', 'durationSec'), ('sentAtEpochMs', 'sentAtEpochMs'))


@dataclass
class SleepingFriendDto(Model):
    user_id: Any = None
    start_sleep_at: Any = None
    __json_keys__: ClassVar[tuple] = (('user_id', 'user_id'), ('start_sleep_at', 'start_sleep_at'))


@dataclass
class LegacyStampDTO(Model):
    id: Any = None
    priority: Any = None
    image_url: Any = None
    image_url_path: Any = None
    stamp_hash: Any = None
    stamp_sound: Any = None
    stamp_sheet_id: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('priority', 'priority'), ('image_url', 'image_url'), ('image_url_path', 'image_url_path'), ('stamp_hash', 'stamp_hash'), ('stamp_sound', 'stamp_sound'), ('stamp_sheet_id', 'stamp_sheet_id'))


@dataclass
class MediaMessage(Model):
    id: Any = None
    uri: Any = None
    mediaType: Any = None
    mainMapMessageWatchLog: Any = None
    location: Any = None
    thumbnailImageUrl: Any = None
    messageMediaType: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uri', 'uri'), ('mediaType', 'mediaType'), ('mainMapMessageWatchLog', 'mainMapMessageWatchLog'), ('location', 'location'), ('thumbnailImageUrl', 'thumbnailImageUrl'), ('messageMediaType', 'messageMediaType'))


@dataclass
class WhatsUpRequestPostRequest(Model):
    user_id: Any = None
    __json_keys__: ClassVar[tuple] = (('user_id', 'user_id'),)


@dataclass
class UrlPathDTO(Model):
    url: Any = None
    path: Any = None
    __json_keys__: ClassVar[tuple] = (('url', 'url'), ('path', 'path'))


@dataclass
class AdFeature(Model):
    width: Any = None
    height: Any = None
    delay: Any = None
    enabled: Any = None
    enabled_countries: Any = None
    __json_keys__: ClassVar[tuple] = (('width', 'width'), ('height', 'height'), ('delay', 'delay'), ('enabled', 'enabled'), ('enabled_countries', 'enabled_countries'))


@dataclass
class SupportTicketsResponse(Model):
    tickets: Any = None
    __json_keys__: ClassVar[tuple] = (('tickets', 'tickets'),)


@dataclass
class MarkedCheckInDTO(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    spot_category: Any = None
    spot_name: Any = None
    platform_location_item: Any = None
    checkin_users: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_category', 'spot_category'), ('spot_name', 'spot_name'), ('platform_location_item', 'platform_location_item'), ('checkin_users', 'checkin_users'))


@dataclass
class DefaultReactionListDTO(Model):
    stamps: Any = None
    __json_keys__: ClassVar[tuple] = (('stamps', 'stamps'),)


@dataclass
class ReverseGeocodesResponse(Model):
    geocodes: Any = None
    __json_keys__: ClassVar[tuple] = (('geocodes', 'geocodes'),)


@dataclass
class RoomResponse(Model):
    room: Any = None
    errors: Any = None
    __json_keys__: ClassVar[tuple] = (('room', 'room'), ('errors', 'errors'))


@dataclass
class RoomWhatsupResponse(Model):
    message: Any = None
    errors: Any = None
    __json_keys__: ClassVar[tuple] = (('message', 'message'), ('errors', 'errors'))


@dataclass
class BoomLocationDto(Model):
    latitude: Any = None
    longitude: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'))


@dataclass
class LocationDTO(Model):
    latitude: Any = None
    longitude: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'))


@dataclass
class CampaignLocationPlacesResponse(Model):
    location_places: Any = None
    landmark_image_url: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('location_places', 'location_places'), ('landmark_image_url', 'landmark_image_url'), ('next_page', 'next_page'))


@dataclass
class UserOriginalStampSheetDTO(Model):
    id: Any = None
    uuid: Any = None
    thumbnail_image_url: Any = None
    is_display_whatsup: Any = None
    user_original_stamps: Any = None
    max_stamp_count: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uuid', 'uuid'), ('thumbnail_image_url', 'thumbnail_image_url'), ('is_display_whatsup', 'is_display_whatsup'), ('user_original_stamps', 'user_original_stamps'), ('max_stamp_count', 'max_stamp_count'))


@dataclass
class Route_GhostModeScreen(Model):
    userId: Any = None
    displayName: Any = None
    profileImage: Any = None
    __json_keys__: ClassVar[tuple] = (('userId', 'userId'), ('displayName', 'displayName'), ('profileImage', 'profileImage'))


@dataclass
class SleepingFriendsResponse(Model):
    friends: Any = None
    __json_keys__: ClassVar[tuple] = (('friends', 'friends'),)


@dataclass
class GroupChatInviteLinkResponse(Model):
    invite_link: Any = None
    __json_keys__: ClassVar[tuple] = (('invite_link', 'invite_link'),)


@dataclass
class SpotCategoryDTO(Model):
    value: Any = None
    label: Any = None
    __json_keys__: ClassVar[tuple] = (('value', 'value'), ('label', 'label'))


@dataclass
class LegacyStampHistoryDTO(Model):
    sheetId: Any = None
    stamp: Any = None
    recommendAd: Any = None
    __json_keys__: ClassVar[tuple] = (('sheetId', 'sheetId'), ('stamp', 'stamp'), ('recommendAd', 'recommendAd'))


@dataclass
class MediaMessageWatchLog(Model):
    id: Any = None
    isReading: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('isReading', 'isReading'))


@dataclass
class WhatsUpRequestPostResponse(Model):
    status: Any = None
    __json_keys__: ClassVar[tuple] = (('status', 'status'),)


@dataclass
class SubscriptionGracePeriodWatchRequest(Model):
    modal_type: Any = None
    __json_keys__: ClassVar[tuple] = (('modal_type', 'modal_type'),)


@dataclass
class FriendsLocationSharingsDTO(Model):
    ambiguous: Any = None
    freeze: Any = None
    errors: Any = None
    __json_keys__: ClassVar[tuple] = (('ambiguous', 'ambiguous'), ('freeze', 'freeze'), ('errors', 'errors'))


@dataclass
class UserResponse(Model):
    user: Any = None
    access_token: Any = None
    errors: Any = None
    __json_keys__: ClassVar[tuple] = (('user', 'user'), ('access_token', 'access_token'), ('errors', 'errors'))


@dataclass
class DefaultStampSheetsDTO(Model):
    stamp_sheets: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_sheets', 'stamp_sheets'),)


@dataclass
class RoomsChannelActionDTO(Model):
    state: Any = None
    text: Any = None
    __json_keys__: ClassVar[tuple] = (('state', 'state'), ('text', 'text'))


@dataclass
class RouteDTO(Model):
    distanceMeters: Any = None
    duration: Any = None
    polyline: Any = None
    __json_keys__: ClassVar[tuple] = (('distanceMeters', 'distanceMeters'), ('duration', 'duration'), ('polyline', 'polyline'))


@dataclass
class SeasonalChallengeConfig(Model):
    name: Any = None
    is_enabled: Any = None
    __json_keys__: ClassVar[tuple] = (('name', 'name'), ('is_enabled', 'is_enabled'))


@dataclass
class WhatsUpOriginalMixedVideoCellDTO(Model):
    user_id: Any = None
    row: Any = None
    col: Any = None
    caption_text: Any = None
    __json_keys__: ClassVar[tuple] = (('user_id', 'user_id'), ('row', 'row'), ('col', 'col'), ('caption_text', 'caption_text'))


@dataclass
class LocationPlaceMediaItemsResponse(Model):
    media_items: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('media_items', 'media_items'), ('next_page', 'next_page'))


@dataclass
class Route_StreakDetailScreen(Model):
    argsJson: Any = None
    __json_keys__: ClassVar[tuple] = (('argsJson', 'argsJson'),)


@dataclass
class WhatsUpUserDTO(Model):
    id: Any = None
    uid: Any = None
    display_name: Any = None
    username: Any = None
    profile_image: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('display_name', 'display_name'), ('username', 'username'), ('profile_image', 'profile_image'))


@dataclass
class RawMessageEventDTO(Model):
    state: Any = None
    text: Any = None
    __json_keys__: ClassVar[tuple] = (('state', 'state'), ('text', 'text'))


@dataclass
class OriginalStampRequest(Model):
    user_original_stamp_id: Any = None
    stamp_count: Any = None
    user_id: Any = None
    __json_keys__: ClassVar[tuple] = (('user_original_stamp_id', 'user_original_stamp_id'), ('stamp_count', 'stamp_count'), ('user_id', 'user_id'))


@dataclass
class UserHiddenDTO(Model):
    hidden_user_ids: Any = None
    errors: Any = None
    __json_keys__: ClassVar[tuple] = (('hidden_user_ids', 'hidden_user_ids'), ('errors', 'errors'))


@dataclass
class MarkedCheckInFriendDTO(Model):
    user: Any = None
    location_place_count: Any = None
    __json_keys__: ClassVar[tuple] = (('user', 'user'), ('location_place_count', 'location_place_count'))


@dataclass
class PostMessageDTO(Model):
    errors: Any = None
    __json_keys__: ClassVar[tuple] = (('errors', 'errors'),)


@dataclass
class FootprintRatesResponse(Model):
    footprint_rates: Any = None
    city_polygon_name: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('footprint_rates', 'footprint_rates'), ('city_polygon_name', 'city_polygon_name'), ('next_page', 'next_page'))


@dataclass
class WhatsUpReactionRequest(Model):
    stamp_id: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_id', 'stamp_id'),)


@dataclass
class RecentlyPlayedMusicResponse(Model):
    recently_played: Any = None
    thirdparty_service: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('recently_played', 'recently_played'), ('thirdparty_service', 'thirdparty_service'), ('next_page', 'next_page'))


@dataclass
class SupportMessageDTO(Model):
    id: Any = None
    sender: Any = None
    kind: Any = None
    body: Any = None
    media_url: Any = None
    thumbnail_url: Any = None
    created_at: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('sender', 'sender'), ('kind', 'kind'), ('body', 'body'), ('media_url', 'media_url'), ('thumbnail_url', 'thumbnail_url'), ('created_at', 'created_at'))


@dataclass
class UserOriginalStampsDTO(Model):
    id: Any = None
    stamp_sound: Any = None
    priority: Any = None
    image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('stamp_sound', 'stamp_sound'), ('priority', 'priority'), ('image_url', 'image_url'))


@dataclass
class RoomsDTO(Model):
    rooms: Any = None
    __json_keys__: ClassVar[tuple] = (('rooms', 'rooms'),)


@dataclass
class WhatsUp(Model):
    whatsup: Any = None
    __json_keys__: ClassVar[tuple] = (('whatsup', 'whatsup'),)


@dataclass
class WhatsUpOriginalMixedVideoDataDTO(Model):
    files: Any = None
    __json_keys__: ClassVar[tuple] = (('files', 'files'),)


@dataclass
class RandomStampResponse(Model):
    image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('image_url', 'image_url'),)


@dataclass
class UpdateLocationSharingRequest(Model):
    location_sharing: Any = None
    __json_keys__: ClassVar[tuple] = (('location_sharing', 'location_sharing'),)


@dataclass
class OriginalStampSheetDTO(Model):
    user_original_stamp_sheet: Any = None
    __json_keys__: ClassVar[tuple] = (('user_original_stamp_sheet', 'user_original_stamp_sheet'),)


@dataclass
class FriendsYourWorldDTO(Model):
    footprint_uuid: Any = None
    user_checkins: Any = None
    __json_keys__: ClassVar[tuple] = (('footprint_uuid', 'footprint_uuid'), ('user_checkins', 'user_checkins'))


@dataclass
class GMTDate(Model):
    seconds: Any = None
    minutes: Any = None
    hours: Any = None
    dayOfWeek: Any = None
    dayOfMonth: Any = None
    dayOfYear: Any = None
    month: Any = None
    year: Any = None
    timestamp: Any = None
    __json_keys__: ClassVar[tuple] = (('seconds', 'seconds'), ('minutes', 'minutes'), ('hours', 'hours'), ('dayOfWeek', 'dayOfWeek'), ('dayOfMonth', 'dayOfMonth'), ('dayOfYear', 'dayOfYear'), ('month', 'month'), ('year', 'year'), ('timestamp', 'timestamp'))


@dataclass
class UserSpotContentDTO(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    name: Any = None
    spot_type: Any = None
    user_checkin_id: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('name', 'name'), ('spot_type', 'spot_type'), ('user_checkin_id', 'user_checkin_id'))


@dataclass
class BestFriendRoute(Model):
    myName: Any = None
    friendName: Any = None
    myThumbUrl: Any = None
    friendThumbUrl: Any = None
    whooId: Any = None
    __json_keys__: ClassVar[tuple] = (('myName', 'myName'), ('friendName', 'friendName'), ('myThumbUrl', 'myThumbUrl'), ('friendThumbUrl', 'friendThumbUrl'), ('whooId', 'whooId'))


@dataclass
class GroupChatUserRequestBody(Model):
    user_ids: Any = None
    __json_keys__: ClassVar[tuple] = (('user_ids', 'user_ids'),)


@dataclass
class Time(Model):
    ms: Any = None
    us: Any = None
    seconds: Any = None
    __json_keys__: ClassVar[tuple] = (('ms', 'ms'), ('us', 'us'), ('seconds', 'seconds'))


@dataclass
class BlockInformationDTO(Model):
    is_blocked: Any = None
    is_blocking: Any = None
    __json_keys__: ClassVar[tuple] = (('is_blocked', 'is_blocked'), ('is_blocking', 'is_blocking'))


@dataclass
class RoomStreakDTO(Model):
    room_id: Any = None
    count: Any = None
    streak_state: Any = None
    badge: Any = None
    __json_keys__: ClassVar[tuple] = (('room_id', 'room_id'), ('count', 'count'), ('streak_state', 'streak_state'), ('badge', 'badge'))


@dataclass
class AppIconGetRoute(Model):
    paramsJson: Any = None
    __json_keys__: ClassVar[tuple] = (('paramsJson', 'paramsJson'),)


@dataclass
class Reaction(Model):
    reactionId: Any = None
    stampId: Any = None
    userId: Any = None
    imageUrl: Any = None
    __json_keys__: ClassVar[tuple] = (('reactionId', 'reactionId'), ('stampId', 'stampId'), ('userId', 'userId'), ('imageUrl', 'imageUrl'))


@dataclass
class SeasonalChallengeMissionDTO(Model):
    mission_type: Any = None
    completed: Any = None
    current_count: Any = None
    required_count: Any = None
    needs_animation: Any = None
    __json_keys__: ClassVar[tuple] = (('mission_type', 'mission_type'), ('completed', 'completed'), ('current_count', 'current_count'), ('required_count', 'required_count'), ('needs_animation', 'needs_animation'))


@dataclass
class FriendRequestDTO(Model):
    user_id: Any = None
    is_in_japan: Any = None
    __json_keys__: ClassVar[tuple] = (('user_id', 'user_id'), ('is_in_japan', 'is_in_japan'))


@dataclass
class WorldRankingFootprintRateDTO(Model):
    user: Any = None
    rank: Any = None
    rate_percent: Any = None
    __json_keys__: ClassVar[tuple] = (('user', 'user'), ('rank', 'rank'), ('rate_percent', 'rate_percent'))


@dataclass
class AuthInfoResponseDTO(Model):
    auth_info: Any = None
    __json_keys__: ClassVar[tuple] = (('auth_info', 'auth_info'),)


@dataclass
class SupportMessageResponse(Model):
    message: Any = None
    __json_keys__: ClassVar[tuple] = (('message', 'message'),)


@dataclass
class CheckInSpotCategoryDTO(Model):
    value: Any = None
    label: Any = None
    __json_keys__: ClassVar[tuple] = (('value', 'value'), ('label', 'label'))


@dataclass
class RoomDTO(Model):
    id: Any = None
    last_message: Any = None
    messaged_at: Any = None
    uid: Any = None
    unreading_message_count: Any = None
    user_states: Any = None
    state: Any = None
    users: Any = None
    room_type: Any = None
    name: Any = None
    icon_image: Any = None
    pinned_at: Any = None
    join_room_state: Any = None
    sort_timestamp: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('last_message', 'last_message'), ('messaged_at', 'messaged_at'), ('uid', 'uid'), ('unreading_message_count', 'unreading_message_count'), ('user_states', 'user_states'), ('state', 'state'), ('users', 'users'), ('room_type', 'room_type'), ('name', 'name'), ('icon_image', 'icon_image'), ('pinned_at', 'pinned_at'), ('join_room_state', 'join_room_state'), ('sort_timestamp', 'sort_timestamp'))


@dataclass
class WatchCountResponse(Model):
    watch_count: Any = None
    profile_images: Any = None
    is_enable_premium: Any = None
    __json_keys__: ClassVar[tuple] = (('watch_count', 'watch_count'), ('profile_images', 'profile_images'), ('is_enable_premium', 'is_enable_premium'))


@dataclass
class Waypoint(Model):
    location: Any = None
    __json_keys__: ClassVar[tuple] = (('location', 'location'),)


@dataclass
class WhatsUpOriginalMixedVideoFileDTO(Model):
    video_url: Any = None
    thumbnail_url: Any = None
    position: Any = None
    __json_keys__: ClassVar[tuple] = (('video_url', 'video_url'), ('thumbnail_url', 'thumbnail_url'), ('position', 'position'))


@dataclass
class WhatsUpReactionStampDTO(Model):
    id: Any = None
    image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('image_url', 'image_url'))


@dataclass
class SendSupportMessageRequest(Model):
    kind: Any = None
    body: Any = None
    media: Any = None
    thumbnail: Any = None
    fcm_token: Any = None
    __json_keys__: ClassVar[tuple] = (('kind', 'kind'), ('body', 'body'), ('media', 'media'), ('thumbnail', 'thumbnail'), ('fcm_token', 'fcm_token'))


@dataclass
class SessionConfigs(Model):
    sessionsEnabled: Any = None
    sessionSamplingRate: Any = None
    sessionTimeoutSeconds: Any = None
    cacheDurationSeconds: Any = None
    cacheUpdatedTimeSeconds: Any = None
    __json_keys__: ClassVar[tuple] = (('sessionsEnabled', 'sessionsEnabled'), ('sessionSamplingRate', 'sessionSamplingRate'), ('sessionTimeoutSeconds', 'sessionTimeoutSeconds'), ('cacheDurationSeconds', 'cacheDurationSeconds'), ('cacheUpdatedTimeSeconds', 'cacheUpdatedTimeSeconds'))


@dataclass
class UpdateMarkedCheckInRequest(Model):
    spot_name: Any = None
    user_ids: Any = None
    __json_keys__: ClassVar[tuple] = (('spot_name', 'spot_name'), ('user_ids', 'user_ids'))


@dataclass
class FriendCheckInUserCheckinDTO(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    spot_category: Any = None
    spot_name: Any = None
    last_stayed_at: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_category', 'spot_category'), ('spot_name', 'spot_name'), ('last_stayed_at', 'last_stayed_at'))


@dataclass
class UserCheckInQuestionDTO(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    horizontal_accuracy: Any = None
    is_friend_registered: Any = None
    is_today_checkin: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('horizontal_accuracy', 'horizontal_accuracy'), ('is_friend_registered', 'is_friend_registered'), ('is_today_checkin', 'is_today_checkin'))


@dataclass
class UserSpotDTO(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    name: Any = None
    spot_type: Any = None
    user_checkin_id: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('name', 'name'), ('spot_type', 'spot_type'), ('user_checkin_id', 'user_checkin_id'))


@dataclass
class InviterUserDTO(Model):
    id: Any = None
    uid: Any = None
    display_name: Any = None
    username: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('display_name', 'display_name'), ('username', 'username'))


@dataclass
class MarkedCheckInFriendsResponse(Model):
    friends: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('friends', 'friends'), ('next_page', 'next_page'))


@dataclass
class BillingStampDTO(Model):
    id: Any = None
    image_url: Any = None
    stamp_hash: Any = None
    priority: Any = None
    file_extension: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('image_url', 'image_url'), ('stamp_hash', 'stamp_hash'), ('priority', 'priority'), ('file_extension', 'file_extension'))


@dataclass
class MemoryHighlightsAvailabilityDTO(Model):
    is_premium_user: Any = None
    month: Any = None
    __json_keys__: ClassVar[tuple] = (('is_premium_user', 'is_premium_user'), ('month', 'month'))


@dataclass
class FootprintUrlDTO(Model):
    urls: Any = None
    __json_keys__: ClassVar[tuple] = (('urls', 'urls'),)


@dataclass
class SupportMessagesResponse(Model):
    messages: Any = None
    __json_keys__: ClassVar[tuple] = (('messages', 'messages'),)


@dataclass
class DefaultIconImage(Model):
    url: Any = None
    key: Any = None
    __json_keys__: ClassVar[tuple] = (('url', 'url'), ('key', 'key'))


@dataclass
class CheckInSpotDTO(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    spot_type: Any = None
    name: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_type', 'spot_type'), ('name', 'name'))


@dataclass
class Route_RequestFriendScreen(Model):
    userJson: Any = None
    fromShake: Any = None
    __json_keys__: ClassVar[tuple] = (('userJson', 'userJson'), ('fromShake', 'fromShake'))


@dataclass
class RoomStreakDetailDTO(Model):
    count: Any = None
    streak_state: Any = None
    badge: Any = None
    freeze_starts_at: Any = None
    freeze_ends_at: Any = None
    __json_keys__: ClassVar[tuple] = (('count', 'count'), ('streak_state', 'streak_state'), ('badge', 'badge'), ('freeze_starts_at', 'freeze_starts_at'), ('freeze_ends_at', 'freeze_ends_at'))


@dataclass
class ReplyOriginalMessageInfo(Model):
    id: Any = None
    uid: Any = None
    isCancel: Any = None
    messageType: Any = None
    isReplyWhatsup: Any = None
    textMessage: Any = None
    mediaMessage: Any = None
    stampMessage: Any = None
    user: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('isCancel', 'isCancel'), ('messageType', 'messageType'), ('isReplyWhatsup', 'isReplyWhatsup'), ('textMessage', 'textMessage'), ('mediaMessage', 'mediaMessage'), ('stampMessage', 'stampMessage'), ('user', 'user'))


@dataclass
class WhatsUpOriginalMixedVideoResponse(Model):
    whatsup_original_mixed_video: Any = None
    __json_keys__: ClassVar[tuple] = (('whatsup_original_mixed_video', 'whatsup_original_mixed_video'),)


@dataclass
class WhatsUpReactionStampsResponse(Model):
    stamps: Any = None
    __json_keys__: ClassVar[tuple] = (('stamps', 'stamps'),)


@dataclass
class FriendCheckInDetailDTO(Model):
    latitude: Any = None
    longitude: Any = None
    spot_category: Any = None
    spot_name: Any = None
    stayed_at: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_category', 'spot_category'), ('spot_name', 'spot_name'), ('stayed_at', 'stayed_at'))


@dataclass
class UpdateRecentlyPlayedMusicRequest(Model):
    service_name: Any = None
    identifier: Any = None
    title: Any = None
    artist_name: Any = None
    cover_image_url: Any = None
    service_uri: Any = None
    duration_sec: Any = None
    is_paused: Any = None
    preview_url: Any = None
    __json_keys__: ClassVar[tuple] = (('service_name', 'service_name'), ('identifier', 'identifier'), ('title', 'title'), ('artist_name', 'artist_name'), ('cover_image_url', 'cover_image_url'), ('service_uri', 'service_uri'), ('duration_sec', 'duration_sec'), ('is_paused', 'is_paused'), ('preview_url', 'preview_url'))


@dataclass
class FriendCheckInUserDTO(Model):
    id: Any = None
    uid: Any = None
    username: Any = None
    display_name: Any = None
    profile_image: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('uid', 'uid'), ('username', 'username'), ('display_name', 'display_name'), ('profile_image', 'profile_image'))


@dataclass
class AuthUserDTO(Model):
    email: Any = None
    __json_keys__: ClassVar[tuple] = (('email', 'email'),)


@dataclass
class MessageStampHistoryDTO(Model):
    stampId: Any = None
    __json_keys__: ClassVar[tuple] = (('stampId', 'stampId'),)


@dataclass
class UserAppIconDTO(Model):
    id: Any = None
    app_icon: Any = None
    icon_state: Any = None
    check_conditions: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('app_icon', 'app_icon'), ('icon_state', 'icon_state'), ('check_conditions', 'check_conditions'))


@dataclass
class UserCheckInQuestionsResponse(Model):
    user_checkins: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('user_checkins', 'user_checkins'), ('next_page', 'next_page'))


@dataclass
class UserLocationsResponse(Model):
    locations: Any = None
    __json_keys__: ClassVar[tuple] = (('locations', 'locations'),)


@dataclass
class Route_UserPageScreen(Model):
    userId: Any = None
    previousUserId: Any = None
    __json_keys__: ClassVar[tuple] = (('userId', 'userId'), ('previousUserId', 'previousUserId'))


@dataclass
class UserSpotResponse(Model):
    spot: Any = None
    __json_keys__: ClassVar[tuple] = (('spot', 'spot'),)


@dataclass
class PlaceSearchItemDTO(Model):
    id: Any = None
    name: Any = None
    address: Any = None
    latitude: Any = None
    longitude: Any = None
    category: Any = None
    identifier: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('name', 'name'), ('address', 'address'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('category', 'category'), ('identifier', 'identifier'))


@dataclass
class MarkedCheckInsResponse(Model):
    user_checkins: Any = None
    __json_keys__: ClassVar[tuple] = (('user_checkins', 'user_checkins'),)


@dataclass
class PolylineDTO(Model):
    encodedPolyline: Any = None
    __json_keys__: ClassVar[tuple] = (('encodedPolyline', 'encodedPolyline'),)


@dataclass
class NearbyFriendRequestDTO(Model):
    is_in_japan: Any = None
    __json_keys__: ClassVar[tuple] = (('is_in_japan', 'is_in_japan'),)


@dataclass
class MemoryHighlightsFriendRankingEntryDTO(Model):
    rank: Any = None
    user: Any = None
    count: Any = None
    __json_keys__: ClassVar[tuple] = (('rank', 'rank'), ('user', 'user'), ('count', 'count'))


@dataclass
class WatchLogItem(Model):
    user: Any = None
    watch_count: Any = None
    watched_at: Any = None
    __json_keys__: ClassVar[tuple] = (('user', 'user'), ('watch_count', 'watch_count'), ('watched_at', 'watched_at'))


@dataclass
class AppIconTypeDTO(Model):
    id: Any = None
    icon_type: Any = None
    friends_condition: Any = None
    login_days_condition: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('icon_type', 'icon_type'), ('friends_condition', 'friends_condition'), ('login_days_condition', 'login_days_condition'))


@dataclass
class WhatsUpContent(Model):
    id: Any = None
    media: Any = None
    media_type: Any = None
    thumbnail_image_url: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('media', 'media'), ('media_type', 'media_type'), ('thumbnail_image_url', 'thumbnail_image_url'))


@dataclass
class AbTestAssignmentResponse(Model):
    active: Any = None
    content: Any = None
    __json_keys__: ClassVar[tuple] = (('active', 'active'), ('content', 'content'))


@dataclass
class LocationNavArg(Model):
    latitude: Any = None
    longitude: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'))


@dataclass
class SessionData(Model):
    sessionDetails: Any = None
    backgroundTime: Any = None
    processDataMap: Any = None
    __json_keys__: ClassVar[tuple] = (('sessionDetails', 'sessionDetails'), ('backgroundTime', 'backgroundTime'), ('processDataMap', 'processDataMap'))


@dataclass
class FriendShipDTO(Model):
    id: Any = None
    friend_id: Any = None
    user_id: Any = None
    holded_at: Any = None
    time_with: Any = None
    state: Any = None
    anniversary: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('friend_id', 'friend_id'), ('user_id', 'user_id'), ('holded_at', 'holded_at'), ('time_with', 'time_with'), ('state', 'state'), ('anniversary', 'anniversary'))


@dataclass
class SuggestSpotRequest(Model):
    spot_type: Any = None
    latitude: Any = None
    longitude: Any = None
    __json_keys__: ClassVar[tuple] = (('spot_type', 'spot_type'), ('latitude', 'latitude'), ('longitude', 'longitude'))


@dataclass
class SupportPresignedUrlDTO(Model):
    file_name: Any = None
    url: Any = None
    path: Any = None
    __json_keys__: ClassVar[tuple] = (('file_name', 'file_name'), ('url', 'url'), ('path', 'path'))


@dataclass
class GooglePlaceDetailsResponse(Model):
    identifier: Any = None
    latitude: Any = None
    longitude: Any = None
    address: Any = None
    name: Any = None
    category: Any = None
    __json_keys__: ClassVar[tuple] = (('identifier', 'identifier'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('address', 'address'), ('name', 'name'), ('category', 'category'))


@dataclass
class DefaultIconImages(Model):
    default_icon_images: Any = None
    __json_keys__: ClassVar[tuple] = (('default_icon_images', 'default_icon_images'),)


@dataclass
class CheckInSpotResponse(Model):
    spot: Any = None
    __json_keys__: ClassVar[tuple] = (('spot', 'spot'),)


@dataclass
class BlockUsersDTO(Model):
    users: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('users', 'users'), ('next_page', 'next_page'))


@dataclass
class StampSheetProductResponseDTO(Model):
    stamp_sheet_products: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_sheet_products', 'stamp_sheet_products'), ('next_page', 'next_page'))


@dataclass
class StampMessage(Model):
    id: Any = None
    stampSheetId: Any = None
    imageUrl: Any = None
    stampHash: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('stampSheetId', 'stampSheetId'), ('imageUrl', 'imageUrl'), ('stampHash', 'stampHash'))


@dataclass
class WhatsUpPresignedUrlResponse(Model):
    url: Any = None
    path: Any = None
    thumbnail_url: Any = None
    thumbnail_path: Any = None
    max_video_seconds: Any = None
    __json_keys__: ClassVar[tuple] = (('url', 'url'), ('path', 'path'), ('thumbnail_url', 'thumbnail_url'), ('thumbnail_path', 'thumbnail_path'), ('max_video_seconds', 'max_video_seconds'))


@dataclass
class WhatsUpReactionSummaryDTO(Model):
    stamp: Any = None
    reaction_count: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp', 'stamp'), ('reaction_count', 'reaction_count'))


@dataclass
class LocationTriggerEventDTO(Model):
    latitude: Any = None
    longitude: Any = None
    title: Any = None
    url: Any = None
    radius_m: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('title', 'title'), ('url', 'url'), ('radius_m', 'radius_m'))


@dataclass
class UpdateRoomRequest(Model):
    icon_image: Any = None
    __json_keys__: ClassVar[tuple] = (('icon_image', 'icon_image'),)


@dataclass
class AuthUserResponseDTO(Model):
    user: Any = None
    errors: Any = None
    __json_keys__: ClassVar[tuple] = (('user', 'user'), ('errors', 'errors'))


@dataclass
class UserAppVersionRequest(Model):
    app_version: Any = None
    __json_keys__: ClassVar[tuple] = (('app_version', 'app_version'),)


@dataclass
class UserCheckInResponse(Model):
    user_checkin: Any = None
    __json_keys__: ClassVar[tuple] = (('user_checkin', 'user_checkin'),)


@dataclass
class UserSpotUpdateBody(Model):
    latitude: Any = None
    longitude: Any = None
    spot_type: Any = None
    name: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_type', 'spot_type'), ('name', 'name'))


@dataclass
class FeatureFlag(Model):
    is_background_location_enabled: Any = None
    network_location: Any = None
    ad_feature: Any = None
    is_map_camera_enabled: Any = None
    route_ui_enabled: Any = None
    use_direct_fgs_start: Any = None
    __json_keys__: ClassVar[tuple] = (('is_background_location_enabled', 'is_background_location_enabled'), ('network_location', 'network_location'), ('ad_feature', 'ad_feature'), ('is_map_camera_enabled', 'is_map_camera_enabled'), ('route_ui_enabled', 'route_ui_enabled'), ('use_direct_fgs_start', 'use_direct_fgs_start'))


@dataclass
class RequestFriendUser(Model):
    id: Any = None
    displayName: Any = None
    profileImage: Any = None
    friendState: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('displayName', 'displayName'), ('profileImage', 'profileImage'), ('friendState', 'friendState'))


@dataclass
class OfJson(Model):
    latitude: Any = None
    longitude: Any = None
    provider: Any = None
    isBatteryCharging: Any = None
    batteryLevel: Any = None
    isNetworkEnabled: Any = None
    isLocationUpdateStaying: Any = None
    startDateOfStay: Any = None
    horizontalAccuracy: Any = None
    speed: Any = None
    bearing: Any = None
    time: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'), ('provider', 'provider'), ('isBatteryCharging', 'isBatteryCharging'), ('batteryLevel', 'batteryLevel'), ('isNetworkEnabled', 'isNetworkEnabled'), ('isLocationUpdateStaying', 'isLocationUpdateStaying'), ('startDateOfStay', 'startDateOfStay'), ('horizontalAccuracy', 'horizontalAccuracy'), ('speed', 'speed'), ('bearing', 'bearing'), ('time', 'time'))


@dataclass
class PremiumUserApiErrorResponse(Model):
    error_code: Any = None
    __json_keys__: ClassVar[tuple] = (('error_code', 'error_code'),)


@dataclass
class RoomStreakResponse(Model):
    streak: Any = None
    __json_keys__: ClassVar[tuple] = (('streak', 'streak'),)


@dataclass
class DisconnectThirdPartyServicesIntegrationRequest(Model):
    service_name: Any = None
    status: Any = None
    __json_keys__: ClassVar[tuple] = (('service_name', 'service_name'), ('status', 'status'))


@dataclass
class MemoryHighlightsFriendRankingResponseDTO(Model):
    month: Any = None
    ranking: Any = None
    __json_keys__: ClassVar[tuple] = (('month', 'month'), ('ranking', 'ranking'))


@dataclass
class NewMessageLinkUriInfoListText(Model):
    message_id: Any = None
    link_uri_info_list: Any = None
    __json_keys__: ClassVar[tuple] = (('message_id', 'message_id'), ('link_uri_info_list', 'link_uri_info_list'))


@dataclass
class SeasonalChallengeStatusResponse(Model):
    challenge_period: Any = None
    missions: Any = None
    __json_keys__: ClassVar[tuple] = (('challenge_period', 'challenge_period'), ('missions', 'missions'))


@dataclass
class LocationPlacesResponse(Model):
    location_places: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('location_places', 'location_places'), ('next_page', 'next_page'))


@dataclass
class SettingAboutDetailRoute(Model):
    ordinal: Any = None
    __json_keys__: ClassVar[tuple] = (('ordinal', 'ordinal'),)


@dataclass
class Route_IconCropScreen(Model):
    image: Any = None
    __json_keys__: ClassVar[tuple] = (('image', 'image'),)


@dataclass
class RecommendStampSheetsDTO(Model):
    stamp_sheet_id: Any = None
    priority: Any = None
    dot_image_url: Any = None
    large_ad_image_url: Any = None
    is_once_bring_front: Any = None
    once_bring_front_cache_key: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp_sheet_id', 'stamp_sheet_id'), ('priority', 'priority'), ('dot_image_url', 'dot_image_url'), ('large_ad_image_url', 'large_ad_image_url'), ('is_once_bring_front', 'is_once_bring_front'), ('once_bring_front_cache_key', 'once_bring_front_cache_key'))


@dataclass
class FriendShipNavArg(Model):
    id: Any = None
    userId: Any = None
    state: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('userId', 'userId'), ('state', 'state'))


@dataclass
class SuggestSpotUserSpotDTO(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    spot_type: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_type', 'spot_type'))


@dataclass
class SupportPresignedUrlsRequest(Model):
    filenames: Any = None
    __json_keys__: ClassVar[tuple] = (('filenames', 'filenames'),)


@dataclass
class MusicDTO(Model):
    site_name: Any = None
    identifier: Any = None
    cover_image_url: Any = None
    title: Any = None
    artist_name: Any = None
    service_uri: Any = None
    played_at: Any = None
    played_end_at: Any = None
    preview_url: Any = None
    __json_keys__: ClassVar[tuple] = (('site_name', 'site_name'), ('identifier', 'identifier'), ('cover_image_url', 'cover_image_url'), ('title', 'title'), ('artist_name', 'artist_name'), ('service_uri', 'service_uri'), ('played_at', 'played_at'), ('played_end_at', 'played_end_at'), ('preview_url', 'preview_url'))


@dataclass
class LatLngDTO(Model):
    latitude: Any = None
    longitude: Any = None
    __json_keys__: ClassVar[tuple] = (('latitude', 'latitude'), ('longitude', 'longitude'))


@dataclass
class ComputeRoutesRequest(Model):
    origin: Any = None
    destination: Any = None
    travelMode: Any = None
    routingPreference: Any = None
    computeAlternativeRoutes: Any = None
    __json_keys__: ClassVar[tuple] = (('origin', 'origin'), ('destination', 'destination'), ('travelMode', 'travelMode'), ('routingPreference', 'routingPreference'), ('computeAlternativeRoutes', 'computeAlternativeRoutes'))


@dataclass
class NearbySearchLocationDTO(Model):
    identifier: Any = None
    latitude: Any = None
    longitude: Any = None
    name: Any = None
    category: Any = None
    __json_keys__: ClassVar[tuple] = (('identifier', 'identifier'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('name', 'name'), ('category', 'category'))


@dataclass
class StreakInfo(Model):
    streakCount: Any = None
    badge: Any = None
    freezeStartsAt: Any = None
    freezeEndsAt: Any = None
    isLinkActive: Any = None
    __json_keys__: ClassVar[tuple] = (('streakCount', 'streakCount'), ('badge', 'badge'), ('freezeStartsAt', 'freezeStartsAt'), ('freezeEndsAt', 'freezeEndsAt'), ('isLinkActive', 'isLinkActive'))


@dataclass
class WhatsUpCreatedResponse(Model):
    whatsup_video: Any = None
    __json_keys__: ClassVar[tuple] = (('whatsup_video', 'whatsup_video'),)


@dataclass
class WhatsUpReactionCatalogStampDTO(Model):
    id: Any = None
    priority: Any = None
    image_url: Any = None
    category: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('priority', 'priority'), ('image_url', 'image_url'), ('category', 'category'))


@dataclass
class WhatsUpReactorDTO(Model):
    stamp: Any = None
    user: Any = None
    __json_keys__: ClassVar[tuple] = (('stamp', 'stamp'), ('user', 'user'))


@dataclass
class AbTestContentDTO(Model):
    id: Any = None
    identifier: Any = None
    thumbnail_url: Any = None
    button_text: Any = None
    button_element_identifier: Any = None
    button_action_type: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('identifier', 'identifier'), ('thumbnail_url', 'thumbnail_url'), ('button_text', 'button_text'), ('button_element_identifier', 'button_element_identifier'), ('button_action_type', 'button_action_type'))


@dataclass
class LocationTriggerEventsResponse(Model):
    trigger_events: Any = None
    __json_keys__: ClassVar[tuple] = (('trigger_events', 'trigger_events'),)


@dataclass
class UploadableUserIds(Model):
    ids: Any = None
    __json_keys__: ClassVar[tuple] = (('ids', 'ids'),)


@dataclass
class UserAppVersionResponse(Model):
    app_version: Any = None
    __json_keys__: ClassVar[tuple] = (('app_version', 'app_version'),)


@dataclass
class UserSpotUpdateRequest(Model):
    user_spot: Any = None
    __json_keys__: ClassVar[tuple] = (('user_spot', 'user_spot'),)


@dataclass
class user_spot(Model):
    id: Any = None
    spot_type: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('spot_type', 'spot_type'))


@dataclass
class PlatformLocationDetailsResponse(Model):
    description: Any = None
    phone_number: Any = None
    address: Any = None
    __json_keys__: ClassVar[tuple] = (('description', 'description'), ('phone_number', 'phone_number'), ('address', 'address'))


@dataclass
class MyCurrentLocationFootprintRateResponse(Model):
    rate_percent: Any = None
    city_polygon_name: Any = None
    __json_keys__: ClassVar[tuple] = (('rate_percent', 'rate_percent'), ('city_polygon_name', 'city_polygon_name'))


@dataclass
class BillingStampSheetDTO(Model):
    id: Any = None
    name: Any = None
    thumbnail_image_url: Any = None
    dot_image_url: Any = None
    description: Any = None
    priority: Any = None
    expires_at: Any = None
    copyright: Any = None
    stamps: Any = None
    author: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('name', 'name'), ('thumbnail_image_url', 'thumbnail_image_url'), ('dot_image_url', 'dot_image_url'), ('description', 'description'), ('priority', 'priority'), ('expires_at', 'expires_at'), ('copyright', 'copyright'), ('stamps', 'stamps'), ('author', 'author'))


@dataclass
class PremiumUserBody(Model):
    starts_at: Any = None
    expires_at: Any = None
    billing_interval: Any = None
    payment_method: Any = None
    purchase_os_type: Any = None
    __json_keys__: ClassVar[tuple] = (('starts_at', 'starts_at'), ('expires_at', 'expires_at'), ('billing_interval', 'billing_interval'), ('payment_method', 'payment_method'), ('purchase_os_type', 'purchase_os_type'))


@dataclass
class MemoryHighlightsLocationPlaceDTO(Model):
    id: Any = None
    name: Any = None
    address: Any = None
    emoji: Any = None
    latitude: Any = None
    longitude: Any = None
    uid: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('name', 'name'), ('address', 'address'), ('emoji', 'emoji'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('uid', 'uid'))


@dataclass
class WatchLogResponse(Model):
    total_count: Any = None
    watch_logs: Any = None
    next_page: Any = None
    __json_keys__: ClassVar[tuple] = (('total_count', 'total_count'), ('watch_logs', 'watch_logs'), ('next_page', 'next_page'))


@dataclass
class StampMessageDTO_response(Model):
    user: Any = None
    sender: Any = None
    stamp: Any = None
    stamp_count: Any = None
    created_at: Any = None
    __json_keys__: ClassVar[tuple] = (('user', 'user'), ('sender', 'sender'), ('stamp', 'stamp'), ('stamp_count', 'stamp_count'), ('created_at', 'created_at'))


@dataclass
class StampSheetProductsDTO(Model):
    id: Any = None
    identifier: Any = None
    is_free: Any = None
    is_japan_only: Any = None
    is_purchased: Any = None
    is_purchasable: Any = None
    stamp_sheet: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('identifier', 'identifier'), ('is_free', 'is_free'), ('is_japan_only', 'is_japan_only'), ('is_purchased', 'is_purchased'), ('is_purchasable', 'is_purchasable'), ('stamp_sheet', 'stamp_sheet'))


@dataclass
class SessionDetails(Model):
    sessionId: Any = None
    firstSessionId: Any = None
    sessionIndex: Any = None
    sessionStartTimestampUs: Any = None
    __json_keys__: ClassVar[tuple] = (('sessionId', 'sessionId'), ('firstSessionId', 'firstSessionId'), ('sessionIndex', 'sessionIndex'), ('sessionStartTimestampUs', 'sessionStartTimestampUs'))


@dataclass
class UpdateUserLocationResponseDTO(Model):
    updating: Any = None
    __json_keys__: ClassVar[tuple] = (('updating', 'updating'),)


@dataclass
class SuggestSpotUserSpotResponse(Model):
    user_spot: Any = None
    __json_keys__: ClassVar[tuple] = (('user_spot', 'user_spot'),)


@dataclass
class UserCheckInSpotDTO(Model):
    id: Any = None
    latitude: Any = None
    longitude: Any = None
    spot_category: Any = None
    spot_name: Any = None
    checkin_count: Any = None
    spot_address: Any = None
    platform_location_item: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('spot_category', 'spot_category'), ('spot_name', 'spot_name'), ('checkin_count', 'checkin_count'), ('spot_address', 'spot_address'), ('platform_location_item', 'platform_location_item'))


@dataclass
class SupportPresignedUrlsResponse(Model):
    urls: Any = None
    __json_keys__: ClassVar[tuple] = (('urls', 'urls'),)


@dataclass
class PlaceSearchResponse(Model):
    location_places: Any = None
    next_offset: Any = None
    __json_keys__: ClassVar[tuple] = (('location_places', 'location_places'), ('next_offset', 'next_offset'))


@dataclass
class RoomStreaksResponse(Model):
    streaks: Any = None
    __json_keys__: ClassVar[tuple] = (('streaks', 'streaks'),)


@dataclass
class ProfileImageResponse(Model):
    profile_image: Any = None
    __json_keys__: ClassVar[tuple] = (('profile_image', 'profile_image'),)


@dataclass
class StampDTO(Model):
    id: Any = None
    priority: Any = None
    image_url: Any = None
    image_url_path: Any = None
    stamp_hash: Any = None
    stamp_sound: Any = None
    stamp_sheet_id: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('priority', 'priority'), ('image_url', 'image_url'), ('image_url_path', 'image_url_path'), ('stamp_hash', 'stamp_hash'), ('stamp_sound', 'stamp_sound'), ('stamp_sheet_id', 'stamp_sheet_id'))


@dataclass
class ComputeRoutesResponse(Model):
    routes: Any = None
    __json_keys__: ClassVar[tuple] = (('routes', 'routes'),)


@dataclass
class NearbySearchLocationsResponse(Model):
    locations: Any = None
    __json_keys__: ClassVar[tuple] = (('locations', 'locations'),)


@dataclass
class StampHistoryDTO(Model):
    sheet_id: Any = None
    stamp_id: Any = None
    is_recommend_ad: Any = None
    __json_keys__: ClassVar[tuple] = (('sheet_id', 'sheet_id'), ('stamp_id', 'stamp_id'), ('is_recommend_ad', 'is_recommend_ad'))


@dataclass
class TextMessage(Model):
    id: Any = None
    body: Any = None
    linkUriInfoList: Any = None
    __json_keys__: ClassVar[tuple] = (('id', 'id'), ('body', 'body'), ('linkUriInfoList', 'linkUriInfoList'))


@dataclass
class AppleMusicTokenRequest(Model):
    access_token: Any = None
    __json_keys__: ClassVar[tuple] = (('access_token', 'access_token'),)


@dataclass
class WhatsUpCurrentSlotStatusResponse(Model):
    unread_count: Any = None
    slot_ends_at: Any = None
    __json_keys__: ClassVar[tuple] = (('unread_count', 'unread_count'), ('slot_ends_at', 'slot_ends_at'))


MODEL_REGISTRY = {
    'app.whoo.data.api.ConnectedServicesLocalDataSource.StoredConnectedServices': StoredConnectedServices,
    'app.whoo.data.api.request.CreateUserCheckInRequest': CreateUserCheckInRequest,
    'app.whoo.data.api.request.UserLocationRequestDTO.UserSpot': UserSpot,
    'app.whoo.data.api.request.CreateUserCheckInRequest.AndroidCheckInData': AndroidCheckInData,
    'app.whoo.data.api.request.EndStayRequestDTO': EndStayRequestDTO,
    'app.whoo.data.api.request.EndStayRequestDTO.StayTimeInfo': StayTimeInfo,
    'app.whoo.data.api.request.SleepWakeupRequestDTO': SleepWakeupRequestDTO,
    'app.whoo.data.api.request.SleepWakeupRequestDTO.DeviceStatus': DeviceStatus,
    'app.whoo.data.api.request.SleepWakeupRequestDTO.UserBattery': UserBattery,
    'app.whoo.data.api.request.SleepWakeupRequestDTO.UserLocation': UserLocation,
    'app.whoo.data.api.request.UnlockStampSheetRequest': UnlockStampSheetRequest,
    'app.whoo.data.api.request.UnlockStampSheetRequest.FriendCount': FriendCount,
    'app.whoo.data.api.request.UpdateUserCheckInRequest': UpdateUserCheckInRequest,
    'app.whoo.data.api.request.UpdateUserCheckInRequest.AndroidCheckInData': AndroidCheckInData_UpdateUserCheckInRequest,
    'app.whoo.data.api.request.UserLocationRequestDTO': UserLocationRequestDTO,
    'app.whoo.data.api.request.UserLocationRequestDTO.AppState': AppState,
    'app.whoo.data.api.request.UserLocationRequestDTO.UserBattery': UserBattery_UserLocationRequestDTO,
    'app.whoo.data.api.request.UserLocationRequestDTO.UserLocation': UserLocation_UserLocationRequestDTO,
    'app.whoo.data.api.response.DefaultReactionListDTO.ReactionDTO': ReactionDTO,
    'app.whoo.data.api.response.MessageEventDTO.AddReaction': AddReaction,
    'app.whoo.data.api.response.MessageStampListDTO.RecommendStampSheet': RecommendStampSheet,
    'app.whoo.data.api.response.WhatsUpReplyMessageVideoResponse': WhatsUpReplyMessageVideoResponse,
    'app.whoo.data.api.response.MessageDTO': MessageDTO,
    'app.whoo.data.api.response.MessageEventDTO.AddReaction.AddReactionText': AddReactionText,
    'app.whoo.data.api.response.WhatsUpReplyMessageVideoResponse.WhatsUpReplyVideoDTO': WhatsUpReplyVideoDTO,
    'app.whoo.data.api.response.MessageDTO.EventDetailDTO': EventDetailDTO,
    'app.whoo.data.api.response.MessageStampListDTO.StampSheet': StampSheet,
    'app.whoo.data.api.response.MessageDTO.EventMessageDTO': EventMessageDTO,
    'app.whoo.data.api.response.MessageEventDTO.Cancel': Cancel,
    'app.whoo.data.api.response.MessageStampListDTO.StampSheet.Stamp': Stamp,
    'app.whoo.data.api.response.MessageEventDTO.Cancel.CancelText': CancelText,
    'app.whoo.data.api.response.MessageDTO.LinkUriInfoDTO': LinkUriInfoDTO,
    'app.whoo.data.api.response.MusicChannelPayload': MusicChannelPayload,
    'app.whoo.data.api.response.MusicChannelPayload.Music': Music,
    'app.whoo.data.api.response.MessageDTO.MediaMessageDTO': MediaMessageDTO,
    'app.whoo.data.api.response.MessageEventDTO.DeleteReaction': DeleteReaction,
    'app.whoo.data.api.response.ReactionListDTO.ReactionDTO': ReactionDTO_ReactionListDTO,
    'app.whoo.data.api.response.MessageDTO.MediaMessageDTO.LocationDataDTO': LocationDataDTO,
    'app.whoo.data.api.response.MessageEventDTO.DeleteReaction.DeleteReactionText': DeleteReactionText,
    'app.whoo.data.api.response.MessageDTO.MediaMessageDTO.MediaMessageWatchLogDTO': MediaMessageWatchLogDTO,
    'app.whoo.data.api.response.MessageEventDTO.NewMessage': NewMessage,
    'app.whoo.data.api.response.RoomsChannelActionDTO.Text': Text,
    'app.whoo.data.api.response.MessageDTO.MessageReadStatusDTO': MessageReadStatusDTO,
    'app.whoo.data.api.response.MessageEventDTO.NewMessage.NewMessageText': NewMessageText,
    'app.whoo.data.api.response.StampPayload': StampPayload,
    'app.whoo.data.api.response.StampPayload.Data': Data,
    'app.whoo.data.api.response.MessageDTO.ReactionDTO': ReactionDTO_MessageDTO,
    'app.whoo.data.api.response.MessageEventDTO.Read': Read,
    'app.whoo.data.api.response.StampPayload.User': User,
    'app.whoo.data.api.response.MessageDTO.ReplyOriginalMessageDTO': ReplyOriginalMessageDTO,
    'app.whoo.data.api.response.MessageEventDTO.Read.ReadingText': ReadingText,
    'app.whoo.data.api.response.ThirdPartyServicesIntegrationStatusResponse.ThirdPartyServiceStatus': ThirdPartyServiceStatus,
    'app.whoo.data.api.response.MessageDTO.StampMessageDTO': StampMessageDTO,
    'app.whoo.data.api.response.MessageEventDTO.Typing': Typing,
    'app.whoo.data.api.response.UserLocationsResponse.UserLocationDTO': UserLocationDTO,
    'app.whoo.data.api.response.MessageDTO.StreakInfoDTO': StreakInfoDTO,
    'app.whoo.data.api.response.UserLocationsResponse.UserLocationDTO.BatteryDTO': BatteryDTO,
    'app.whoo.data.api.response.MessageReactionRequest': MessageReactionRequest,
    'app.whoo.data.api.response.MessageDTO.TextMessageDTO': TextMessageDTO,
    'app.whoo.data.api.response.MessageReactionRequest.MessageReaction': MessageReaction,
    'app.whoo.data.api.spotify.request.SpotifyConnectStateRegisterRequest': SpotifyConnectStateRegisterRequest,
    'app.whoo.data.api.spotify.request.SpotifyConnectStateRegisterRequest.Capabilities': Capabilities,
    'app.whoo.data.api.spotify.request.SpotifyConnectStateRegisterRequest.Device': Device,
    'app.whoo.data.api.spotify.request.SpotifyConnectStateRegisterRequest.DeviceInfo': DeviceInfo,
    'boom': boom,
    'check_in_spot': check_in_spot,
    'comeback': comeback,
    'focus_friend_with_stamp_sheet': focus_friend_with_stamp_sheet,
    'friend_check_in': friend_check_in,
    'friend_icon_change': friend_icon_change,
    'place': place,
    'same_landmark_friend_checkin': same_landmark_friend_checkin,
    'short_video_timeline': short_video_timeline,
    'tagged_friend_checkin': tagged_friend_checkin,
    'watch_log': watch_log,
    'app.whoo.ui.setting.AppIconGetDialogFragment.AppIconGetDialogParams': AppIconGetDialogParams,
    'app.whoo.ui.streak.StreakDetailArgs.Active': Active,
    'app.whoo.ui.streak.StreakDetailArgs.Expired': Expired,
    'app.whoo.data.api.response.LocationPlaceCampaignDTO': LocationPlaceCampaignDTO,
    'app.whoo.ui.originalstamp.CreateOriginalStampScreen.Route': Route,
    'app.whoo.data.api.response.FriendCheckInsResponse': FriendCheckInsResponse,
    'app.whoo.data.api.response.RecommendUserSpotDTO': RecommendUserSpotDTO,
    'app.whoo.data.api.response.AuthInfoDTO': AuthInfoDTO,
    'app.whoo.data.api.response.AuthorDTO': AuthorDTO,
    'app.whoo.data.api.response.UserSpotsDTO': UserSpotsDTO,
    'app.whoo.data.api.response.JoinRoomDTO': JoinRoomDTO,
    'com.google.firebase.sessions.ProcessData': ProcessData,
    'app.whoo.data.api.response.MemoryHighlightsLocationPlaceRankingEntryDTO': MemoryHighlightsLocationPlaceRankingEntryDTO,
    'app.whoo.data.api.response.WatchLogUser': WatchLogUser,
    'app.whoo.data.api.request.PurchaseVerificationRequest': PurchaseVerificationRequest,
    'app.whoo.data.api.response.FriendActionDTO': FriendActionDTO,
    'app.whoo.data.api.response.FriendCheckInItemDTO': FriendCheckInItemDTO,
    'app.whoo.data.api.response.RecentlyPlayedItemDTO': RecentlyPlayedItemDTO,
    'app.whoo.data.api.request.UpdateWhatsUpCaptionRequest': UpdateWhatsUpCaptionRequest,
    'app.whoo.data.api.request.SuggestUsernameRequest': SuggestUsernameRequest,
    'app.whoo.data.api.response.MessageStampListDTO': MessageStampListDTO,
    'app.whoo.data.api.amazonmusic.AmazonMusicAuthState': AmazonMusicAuthState,
    'app.whoo.data.api.response.CheckinUserDTO': CheckinUserDTO,
    'app.whoo.data.api.response.MyFootprintRateResponse': MyFootprintRateResponse,
    'app.whoo.data.api.response.PremiumUserResponse': PremiumUserResponse,
    'app.whoo.data.api.spotify.response.SpotifyAccessTokenResponse': SpotifyAccessTokenResponse,
    'app.whoo.data.api.response.BoomUserDto': BoomUserDto,
    'app.whoo.data.api.response.StampMessageUserDTO': StampMessageUserDTO,
    'app.whoo.data.database.entity.MessageEntity.User': User_MessageEntity,
    'app.whoo.data.api.response.WhatsUpDTO': WhatsUpDTO,
    'app.whoo.data.api.response.WhatsUpReactorsResponse': WhatsUpReactorsResponse,
    'app.whoo.data.api.response.LocationPlaceCampaignDetailDTO': LocationPlaceCampaignDetailDTO,
    'app.whoo.data.api.response.WhatsUpWithUserDTO': WhatsUpWithUserDTO,
    'app.whoo.data.api.request.RecommendUserSpotRequest': RecommendUserSpotRequest,
    'app.whoo.data.api.request.ActivateThirdPartyServicesRequest': ActivateThirdPartyServicesRequest,
    'app.whoo.data.api.response.ErrorsDTO': ErrorsDTO,
    'app.whoo.data.api.response.UserCheckInSpotsResponse': UserCheckInSpotsResponse,
    'app.whoo.data.api.response.ShouldSuggestSpotResponse': ShouldSuggestSpotResponse,
    'app.whoo.data.api.response.BannerAutoRefreshConfig': BannerAutoRefreshConfig,
    'app.whoo.data.api.response.RoomUserDTO': RoomUserDTO,
    'app.whoo.data.api.response.MemoryHighlightsLocationPlacesRankingResponseDTO': MemoryHighlightsLocationPlacesRankingResponseDTO,
    'app.whoo.data.database.entity.MessageEntity.Detail': Detail,
    'app.whoo.data.api.response.NowPlayingMusicResponse': NowPlayingMusicResponse,
    'app.whoo.location.telemetry.spool.RawLocationRecord': RawLocationRecord,
    'app.whoo.data.api.request.LocationSharingBody': LocationSharingBody,
    'app.whoo.ui.setting.FriendAppealIconCropScreen.Route': Route_FriendAppealIconCropScreen,
    'app.whoo.data.api.response.UploadFootprintUrlDTO': UploadFootprintUrlDTO,
    'app.whoo.data.api.response.SuggestUsernameResponse': SuggestUsernameResponse,
    'app.whoo.data.api.request.CheckinUsersRequest': CheckinUsersRequest,
    'app.whoo.data.api.response.MyIconRingResponse': MyIconRingResponse,
    'app.whoo.data.api.response.NearbyUserDTO': NearbyUserDTO,
    'app.whoo.data.api.response.StampMessagesDTO': StampMessagesDTO,
    'app.whoo.data.api.response.LocationPlaceCampaignsResponse': LocationPlaceCampaignsResponse,
    'app.whoo.data.api.response.ReactionListDTO': ReactionListDTO,
    'app.whoo.data.api.response.User': User_response,
    'user_checkin': user_checkin,
    'app.whoo.data.api.response.UserCheckInsResponse': UserCheckInsResponse,
    'app.whoo.data.api.response.PlatformLocationItemDTO': PlatformLocationItemDTO,
    'app.whoo.data.api.response.VersionControlDTO': VersionControlDTO,
    'app.whoo.data.api.request.PremiumUserSetting': PremiumUserSetting,
    'app.whoo.data.api.response.MemoryHighlightsTimeWithUsersEntryDTO': MemoryHighlightsTimeWithUsersEntryDTO,
    'app.whoo.data.api.response.FootprintDownloadStatusResponse': FootprintDownloadStatusResponse,
    'app.whoo.data.api.response.FootprintRateWorldRankingResponse': FootprintRateWorldRankingResponse,
    'app.whoo.data.database.entity.MessageEntity.EventMessage': EventMessage,
    'app.whoo.data.featureflag.WhatsUpReminderConfigDTO': WhatsUpReminderConfigDTO,
    'app.whoo.data.api.response.WhatsUpStatusErrorResponse': WhatsUpStatusErrorResponse,
    'app.whoo.data.api.response.LocationSharingDTO': LocationSharingDTO,
    'app.whoo.data.api.response.UploadMediaUrlDTO': UploadMediaUrlDTO,
    'app.whoo.data.api.response.FriendDTO': FriendDTO,
    'app.whoo.data.api.response.CampaignBannerResponse': CampaignBannerResponse,
    'app.whoo.data.api.request.ActivityLogRequest': ActivityLogRequest,
    'app.whoo.data.api.response.GeocodeCenterDTO': GeocodeCenterDTO,
    'app.whoo.data.api.request.PinnedRoomRequestBody': PinnedRoomRequestBody,
    'app.whoo.data.api.response.CheckinUsersResponse': CheckinUsersResponse,
    'app.whoo.data.api.response.ThirdPartyServiceStatusDTO': ThirdPartyServiceStatusDTO,
    'app.whoo.data.api.response.RoomUsersResponse': RoomUsersResponse,
    'app.whoo.data.api.response.BoomFriendLocationsResponse': BoomFriendLocationsResponse,
    'app.whoo.ui.originalstamp.CompletionOriginalStampRoute': CompletionOriginalStampRoute,
    'app.whoo.data.api.response.LocationPlaceDTO': LocationPlaceDTO,
    'app.whoo.data.api.response.FriendCheckInLocationDTO': FriendCheckInLocationDTO,
    'app.whoo.data.api.response.FriendsDTO': FriendsDTO,
    'app.whoo.data.api.request.UserAccount': UserAccount,
    'app.whoo.data.api.response.PlatformLocationItemResponse': PlatformLocationItemResponse,
    'app.whoo.data.api.response.BannerInfoDTO': BannerInfoDTO,
    'app.whoo.data.api.request.PremiumUserSettingsRequest': PremiumUserSettingsRequest,
    'app.whoo.data.api.request.MediaUploadRequest': MediaUploadRequest,
    'app.whoo.data.api.response.MemoryHighlightsTimeWithUsersRankingResponseDTO': MemoryHighlightsTimeWithUsersRankingResponseDTO,
    'app.whoo.data.api.response.BumpResponse': BumpResponse,
    'app.whoo.data.database.entity.MessageEntity.LinkUriInfo': LinkUriInfo,
    'app.whoo.data.api.response.WhatsUpStatusResponse': WhatsUpStatusResponse,
    'app.whoo.data.api.request.CreateSupportTicketRequest': CreateSupportTicketRequest,
    'app.whoo.data.api.response.SettingBannerResponse': SettingBannerResponse,
    'app.whoo.data.api.response.UploadOriginalStampsUrlResponse': UploadOriginalStampsUrlResponse,
    'app.whoo.data.api.response.FriendDetailDTO': FriendDetailDTO,
    'app.whoo.data.api.response.UserCheckInDetailResponse': UserCheckInDetailResponse,
    'app.whoo.data.api.response.SupportTicketDTO': SupportTicketDTO,
    'app.whoo.data.api.response.GeocodeDTO': GeocodeDTO,
    'app.whoo.data.api.response.CheckinedUserDTO': CheckinedUserDTO,
    'app.whoo.data.api.response.RoomInvitationDTO': RoomInvitationDTO,
    'app.whoo.data.api.request.RoomRequestBody': RoomRequestBody,
    'app.whoo.data.api.request.RoomWhatsupBody': RoomWhatsupBody,
    'app.whoo.data.api.spotify.response.SpotifyApresolveResponse': SpotifyApresolveResponse,
    'app.whoo.data.pref.LegacyRecommendAdDTO': LegacyRecommendAdDTO,
    'app.whoo.data.api.response.FootprintRateDTO': FootprintRateDTO,
    'app.whoo.data.api.request.NearbyUsersDiscoveryRequest': NearbyUsersDiscoveryRequest,
    'app.whoo.data.api.response.WhatsUpMixedVideoExistsResponse': WhatsUpMixedVideoExistsResponse,
    'app.whoo.ui.setting.AuthInfoEditRoute': AuthInfoEditRoute,
    'app.whoo.data.api.response.FriendsIconRingItem': FriendsIconRingItem,
    'app.whoo.data.api.response.CampaignLocationPlaceDTO': CampaignLocationPlaceDTO,
    'app.whoo.data.api.response.MessagesDTO': MessagesDTO,
    'app.whoo.data.api.response.UserDTO': UserDTO,
    'app.whoo.data.api.response.RegisteredSpotResponse': RegisteredSpotResponse,
    'app.whoo.data.api.response.ThirdPartyServicesIntegrationStatusResponse': ThirdPartyServicesIntegrationStatusResponse,
    'app.whoo.ui.originalstamp.DeleteOriginalStampScreen.Route': Route_DeleteOriginalStampScreen,
    'app.whoo.data.api.response.MemoryHighlightsUserDTO': MemoryHighlightsUserDTO,
    'app.whoo.data.api.response.StampSheetDTO': StampSheetDTO,
    'app.whoo.ui.setting.AppIconChangeRoute': AppIconChangeRoute,
    'app.whoo.data.database.entity.MessageEntity.Location': Location,
    'app.whoo.data.api.response.StampSheetsDTO': StampSheetsDTO,
    'app.whoo.ui.qr.QrScreen.Route': Route_QrScreen,
    'app.whoo.data.api.request.Location': Location_request,
    'app.whoo.data.api.response.WhatsUpRequestPostErrorResponse': WhatsUpRequestPostErrorResponse,
    'app.whoo.data.api.response.LocationPlaceMediaItemDTO': LocationPlaceMediaItemDTO,
    'app.whoo.data.api.response.FriendCheckInResponse': FriendCheckInResponse,
    'app.whoo.data.api.response.UploadProfileImageUrlDTO': UploadProfileImageUrlDTO,
    'app.whoo.data.api.response.SubscriptionGracePeriodBody': SubscriptionGracePeriodBody,
    'app.whoo.data.api.request.SupportClientContext': SupportClientContext,
    'app.whoo.data.api.response.SupportTicketResponse': SupportTicketResponse,
    'app.whoo.model.UserNavArg': UserNavArg,
    'app.whoo.data.api.request.ChangeProfileImageRequest': ChangeProfileImageRequest,
    'app.whoo.data.api.response.MarkedCheckInCheckinUserDTO': MarkedCheckInCheckinUserDTO,
    'app.whoo.data.api.response.RoomInvitationResponse': RoomInvitationResponse,
    'app.whoo.data.api.request.RoomRequestBodyFields': RoomRequestBodyFields,
    'app.whoo.location.telemetry.upload.PresignedUrlResponse': PresignedUrlResponse,
    'app.whoo.data.api.request.RoomWhatsupBodyData': RoomWhatsupBodyData,
    'app.whoo.data.api.response.NearbyUsersDiscoveryResponse': NearbyUsersDiscoveryResponse,
    'app.whoo.data.api.response.WhatsUpMyReactionDTO': WhatsUpMyReactionDTO,
    'app.whoo.data.api.response.WhatsUpTimelineResponse': WhatsUpTimelineResponse,
    'app.whoo.data.api.request.CreateWhatsUpRequest': CreateWhatsUpRequest,
    'app.whoo.data.api.response.RecommendUserSpotsResponse': RecommendUserSpotsResponse,
    'app.whoo.data.api.response.FriendsIconRingsResponse': FriendsIconRingsResponse,
    'app.whoo.data.api.response.UserDetailDTO': UserDetailDTO,
    'app.whoo.data.api.amazonmusic.AmazonMusicLastSentTrackLocalDataSource.SavedTrack': SavedTrack,
    'app.whoo.data.api.response.SleepingFriendDto': SleepingFriendDto,
    'app.whoo.data.pref.LegacyStampDTO': LegacyStampDTO,
    'app.whoo.data.database.entity.MessageEntity.MediaMessage': MediaMessage,
    'app.whoo.data.api.request.WhatsUpRequestPostRequest': WhatsUpRequestPostRequest,
    'app.whoo.data.api.response.UrlPathDTO': UrlPathDTO,
    'app.whoo.data.api.response.AdFeature': AdFeature,
    'app.whoo.data.api.response.SupportTicketsResponse': SupportTicketsResponse,
    'app.whoo.data.api.response.MarkedCheckInDTO': MarkedCheckInDTO,
    'app.whoo.data.api.response.DefaultReactionListDTO': DefaultReactionListDTO,
    'app.whoo.data.api.response.ReverseGeocodesResponse': ReverseGeocodesResponse,
    'app.whoo.data.api.response.RoomResponse': RoomResponse,
    'app.whoo.data.api.response.RoomWhatsupResponse': RoomWhatsupResponse,
    'app.whoo.data.api.response.BoomLocationDto': BoomLocationDto,
    'app.whoo.data.api.response.LocationDTO': LocationDTO,
    'app.whoo.data.api.response.CampaignLocationPlacesResponse': CampaignLocationPlacesResponse,
    'app.whoo.data.api.response.UserOriginalStampSheetDTO': UserOriginalStampSheetDTO,
    'app.whoo.ui.ghostmode.GhostModeScreen.Route': Route_GhostModeScreen,
    'app.whoo.data.api.response.SleepingFriendsResponse': SleepingFriendsResponse,
    'app.whoo.data.api.response.GroupChatInviteLinkResponse': GroupChatInviteLinkResponse,
    'app.whoo.data.api.response.SpotCategoryDTO': SpotCategoryDTO,
    'app.whoo.data.pref.LegacyStampHistoryDTO': LegacyStampHistoryDTO,
    'app.whoo.data.database.entity.MessageEntity.MediaMessageWatchLog': MediaMessageWatchLog,
    'app.whoo.data.api.response.WhatsUpRequestPostResponse': WhatsUpRequestPostResponse,
    'app.whoo.data.api.request.SubscriptionGracePeriodWatchRequest': SubscriptionGracePeriodWatchRequest,
    'app.whoo.data.api.response.FriendsLocationSharingsDTO': FriendsLocationSharingsDTO,
    'app.whoo.data.api.response.UserResponse': UserResponse,
    'app.whoo.data.api.response.DefaultStampSheetsDTO': DefaultStampSheetsDTO,
    'app.whoo.data.api.response.RoomsChannelActionDTO': RoomsChannelActionDTO,
    'app.whoo.data.api.response.RouteDTO': RouteDTO,
    'app.whoo.data.api.response.SeasonalChallengeConfig': SeasonalChallengeConfig,
    'app.whoo.data.api.response.WhatsUpOriginalMixedVideoCellDTO': WhatsUpOriginalMixedVideoCellDTO,
    'app.whoo.data.api.response.LocationPlaceMediaItemsResponse': LocationPlaceMediaItemsResponse,
    'app.whoo.ui.streak.StreakDetailScreen.Route': Route_StreakDetailScreen,
    'app.whoo.data.api.response.WhatsUpUserDTO': WhatsUpUserDTO,
    'app.whoo.data.api.response.RawMessageEventDTO': RawMessageEventDTO,
    'app.whoo.data.api.request.OriginalStampRequest': OriginalStampRequest,
    'app.whoo.data.api.response.UserHiddenDTO': UserHiddenDTO,
    'app.whoo.data.api.response.MarkedCheckInFriendDTO': MarkedCheckInFriendDTO,
    'app.whoo.data.api.response.PostMessageDTO': PostMessageDTO,
    'app.whoo.data.api.response.FootprintRatesResponse': FootprintRatesResponse,
    'app.whoo.data.api.request.WhatsUpReactionRequest': WhatsUpReactionRequest,
    'app.whoo.data.api.response.RecentlyPlayedMusicResponse': RecentlyPlayedMusicResponse,
    'app.whoo.data.api.response.SupportMessageDTO': SupportMessageDTO,
    'app.whoo.data.api.response.UserOriginalStampsDTO': UserOriginalStampsDTO,
    'app.whoo.data.api.response.RoomsDTO': RoomsDTO,
    'app.whoo.data.api.WhatsUp': WhatsUp,
    'app.whoo.data.api.response.WhatsUpOriginalMixedVideoDataDTO': WhatsUpOriginalMixedVideoDataDTO,
    'app.whoo.data.api.response.RandomStampResponse': RandomStampResponse,
    'app.whoo.data.api.request.UpdateLocationSharingRequest': UpdateLocationSharingRequest,
    'app.whoo.data.api.response.OriginalStampSheetDTO': OriginalStampSheetDTO,
    'app.whoo.data.api.response.FriendsYourWorldDTO': FriendsYourWorldDTO,
    'io.ktor.util.date.GMTDate': GMTDate,
    'app.whoo.data.api.response.UserSpotContentDTO': UserSpotContentDTO,
    'app.whoo.ui.mypage.BestFriendRoute': BestFriendRoute,
    'app.whoo.data.api.request.GroupChatUserRequestBody': GroupChatUserRequestBody,
    'com.google.firebase.sessions.Time': Time,
    'app.whoo.data.api.response.BlockInformationDTO': BlockInformationDTO,
    'app.whoo.data.api.response.RoomStreakDTO': RoomStreakDTO,
    'app.whoo.ui.setting.AppIconGetRoute': AppIconGetRoute,
    'app.whoo.data.database.entity.MessageEntity.Reaction': Reaction,
    'app.whoo.data.api.response.SeasonalChallengeMissionDTO': SeasonalChallengeMissionDTO,
    'app.whoo.data.api.request.FriendRequestDTO': FriendRequestDTO,
    'app.whoo.data.api.response.WorldRankingFootprintRateDTO': WorldRankingFootprintRateDTO,
    'app.whoo.data.api.response.AuthInfoResponseDTO': AuthInfoResponseDTO,
    'app.whoo.data.api.response.SupportMessageResponse': SupportMessageResponse,
    'app.whoo.data.api.response.CheckInSpotCategoryDTO': CheckInSpotCategoryDTO,
    'app.whoo.data.api.response.RoomDTO': RoomDTO,
    'app.whoo.data.api.response.WatchCountResponse': WatchCountResponse,
    'app.whoo.data.api.request.Waypoint': Waypoint,
    'app.whoo.data.api.response.WhatsUpOriginalMixedVideoFileDTO': WhatsUpOriginalMixedVideoFileDTO,
    'app.whoo.data.api.response.WhatsUpReactionStampDTO': WhatsUpReactionStampDTO,
    'app.whoo.data.api.request.SendSupportMessageRequest': SendSupportMessageRequest,
    'com.google.firebase.sessions.settings.SessionConfigs': SessionConfigs,
    'app.whoo.data.api.request.UpdateMarkedCheckInRequest': UpdateMarkedCheckInRequest,
    'app.whoo.data.api.response.FriendCheckInUserCheckinDTO': FriendCheckInUserCheckinDTO,
    'app.whoo.data.api.response.UserCheckInQuestionDTO': UserCheckInQuestionDTO,
    'app.whoo.data.api.response.UserSpotDTO': UserSpotDTO,
    'app.whoo.data.api.response.InviterUserDTO': InviterUserDTO,
    'app.whoo.data.api.response.MarkedCheckInFriendsResponse': MarkedCheckInFriendsResponse,
    'app.whoo.data.api.response.BillingStampDTO': BillingStampDTO,
    'app.whoo.data.api.response.MemoryHighlightsAvailabilityDTO': MemoryHighlightsAvailabilityDTO,
    'app.whoo.data.api.response.FootprintUrlDTO': FootprintUrlDTO,
    'app.whoo.data.api.response.SupportMessagesResponse': SupportMessagesResponse,
    'app.whoo.data.api.response.DefaultIconImage': DefaultIconImage,
    'app.whoo.data.api.response.CheckInSpotDTO': CheckInSpotDTO,
    'app.whoo.ui.addfriend.RequestFriendScreen.Route': Route_RequestFriendScreen,
    'app.whoo.data.api.response.RoomStreakDetailDTO': RoomStreakDetailDTO,
    'app.whoo.data.database.entity.MessageEntity.ReplyOriginalMessageInfo': ReplyOriginalMessageInfo,
    'app.whoo.data.api.response.WhatsUpOriginalMixedVideoResponse': WhatsUpOriginalMixedVideoResponse,
    'app.whoo.data.api.response.WhatsUpReactionStampsResponse': WhatsUpReactionStampsResponse,
    'app.whoo.data.api.response.FriendCheckInDetailDTO': FriendCheckInDetailDTO,
    'app.whoo.data.api.request.UpdateRecentlyPlayedMusicRequest': UpdateRecentlyPlayedMusicRequest,
    'app.whoo.data.api.response.FriendCheckInUserDTO': FriendCheckInUserDTO,
    'app.whoo.data.api.response.AuthUserDTO': AuthUserDTO,
    'app.whoo.data.api.response.MessageStampHistoryDTO': MessageStampHistoryDTO,
    'app.whoo.data.api.response.UserAppIconDTO': UserAppIconDTO,
    'app.whoo.data.api.response.UserCheckInQuestionsResponse': UserCheckInQuestionsResponse,
    'app.whoo.data.api.response.UserLocationsResponse': UserLocationsResponse,
    'app.whoo.ui.userpage.UserPageScreen.Route': Route_UserPageScreen,
    'app.whoo.data.api.response.UserSpotResponse': UserSpotResponse,
    'app.whoo.data.api.response.PlaceSearchItemDTO': PlaceSearchItemDTO,
    'app.whoo.data.api.response.MarkedCheckInsResponse': MarkedCheckInsResponse,
    'app.whoo.data.api.response.PolylineDTO': PolylineDTO,
    'app.whoo.data.api.request.NearbyFriendRequestDTO': NearbyFriendRequestDTO,
    'app.whoo.data.api.response.MemoryHighlightsFriendRankingEntryDTO': MemoryHighlightsFriendRankingEntryDTO,
    'app.whoo.data.api.response.WatchLogItem': WatchLogItem,
    'app.whoo.data.api.response.AppIconTypeDTO': AppIconTypeDTO,
    'app.whoo.data.api.WhatsUpContent': WhatsUpContent,
    'app.whoo.data.api.response.AbTestAssignmentResponse': AbTestAssignmentResponse,
    'app.whoo.model.LocationNavArg': LocationNavArg,
    'com.google.firebase.sessions.SessionData': SessionData,
    'app.whoo.data.api.response.FriendShipDTO': FriendShipDTO,
    'app.whoo.data.api.request.SuggestSpotRequest': SuggestSpotRequest,
    'app.whoo.data.api.response.SupportPresignedUrlDTO': SupportPresignedUrlDTO,
    'app.whoo.data.api.response.GooglePlaceDetailsResponse': GooglePlaceDetailsResponse,
    'app.whoo.data.api.response.DefaultIconImages': DefaultIconImages,
    'app.whoo.data.api.response.CheckInSpotResponse': CheckInSpotResponse,
    'app.whoo.data.api.response.BlockUsersDTO': BlockUsersDTO,
    'app.whoo.data.api.response.StampSheetProductResponseDTO': StampSheetProductResponseDTO,
    'app.whoo.data.database.entity.MessageEntity.StampMessage': StampMessage,
    'app.whoo.data.api.response.WhatsUpPresignedUrlResponse': WhatsUpPresignedUrlResponse,
    'app.whoo.data.api.response.WhatsUpReactionSummaryDTO': WhatsUpReactionSummaryDTO,
    'app.whoo.data.api.response.LocationTriggerEventDTO': LocationTriggerEventDTO,
    'app.whoo.data.api.request.UpdateRoomRequest': UpdateRoomRequest,
    'app.whoo.data.api.response.AuthUserResponseDTO': AuthUserResponseDTO,
    'app.whoo.data.api.request.UserAppVersionRequest': UserAppVersionRequest,
    'app.whoo.data.api.response.UserCheckInResponse': UserCheckInResponse,
    'app.whoo.data.api.response.UserSpotUpdateBody': UserSpotUpdateBody,
    'app.whoo.data.api.response.FeatureFlag': FeatureFlag,
    'app.whoo.ui.addfriend.RequestFriendUser': RequestFriendUser,
    'app.whoo.model.DeviceInfo.OfJson': OfJson,
    'app.whoo.data.api.response.PremiumUserApiErrorResponse': PremiumUserApiErrorResponse,
    'app.whoo.data.api.response.RoomStreakResponse': RoomStreakResponse,
    'app.whoo.data.api.request.DisconnectThirdPartyServicesIntegrationRequest': DisconnectThirdPartyServicesIntegrationRequest,
    'app.whoo.data.api.response.MemoryHighlightsFriendRankingResponseDTO': MemoryHighlightsFriendRankingResponseDTO,
    'app.whoo.data.api.response.MessageEventDTO.NewTextMessageLinkUriInfoList.NewMessageLinkUriInfoListText': NewMessageLinkUriInfoListText,
    'app.whoo.data.api.response.SeasonalChallengeStatusResponse': SeasonalChallengeStatusResponse,
    'app.whoo.data.api.response.LocationPlacesResponse': LocationPlacesResponse,
    'app.whoo.ui.setting.SettingAboutDetailRoute': SettingAboutDetailRoute,
    'app.whoo.ui.setting.IconCropScreen.Route': Route_IconCropScreen,
    'app.whoo.data.api.response.RecommendStampSheetsDTO': RecommendStampSheetsDTO,
    'app.whoo.model.FriendShipNavArg': FriendShipNavArg,
    'app.whoo.data.api.response.SuggestSpotUserSpotDTO': SuggestSpotUserSpotDTO,
    'app.whoo.data.api.request.SupportPresignedUrlsRequest': SupportPresignedUrlsRequest,
    'app.whoo.data.api.response.MusicDTO': MusicDTO,
    'app.whoo.data.api.request.LatLngDTO': LatLngDTO,
    'app.whoo.data.api.request.ComputeRoutesRequest': ComputeRoutesRequest,
    'app.whoo.data.api.response.NearbySearchLocationDTO': NearbySearchLocationDTO,
    'app.whoo.data.database.entity.MessageEntity.StreakInfo': StreakInfo,
    'app.whoo.data.api.response.WhatsUpCreatedResponse': WhatsUpCreatedResponse,
    'app.whoo.data.api.response.WhatsUpReactionCatalogStampDTO': WhatsUpReactionCatalogStampDTO,
    'app.whoo.data.api.response.WhatsUpReactorDTO': WhatsUpReactorDTO,
    'app.whoo.data.api.response.AbTestContentDTO': AbTestContentDTO,
    'app.whoo.data.api.response.LocationTriggerEventsResponse': LocationTriggerEventsResponse,
    'app.whoo.data.api.response.UploadableUserIds': UploadableUserIds,
    'app.whoo.data.api.response.UserAppVersionResponse': UserAppVersionResponse,
    'app.whoo.data.api.response.UserSpotUpdateRequest': UserSpotUpdateRequest,
    'user_spot': user_spot,
    'app.whoo.data.api.response.PlatformLocationDetailsResponse': PlatformLocationDetailsResponse,
    'app.whoo.data.api.response.MyCurrentLocationFootprintRateResponse': MyCurrentLocationFootprintRateResponse,
    'app.whoo.data.api.response.BillingStampSheetDTO': BillingStampSheetDTO,
    'app.whoo.data.api.response.PremiumUserBody': PremiumUserBody,
    'app.whoo.data.api.response.MemoryHighlightsLocationPlaceDTO': MemoryHighlightsLocationPlaceDTO,
    'app.whoo.data.api.response.WatchLogResponse': WatchLogResponse,
    'app.whoo.data.api.response.StampMessageDTO': StampMessageDTO_response,
    'app.whoo.data.api.response.StampSheetProductsDTO': StampSheetProductsDTO,
    'com.google.firebase.sessions.SessionDetails': SessionDetails,
    'app.whoo.data.api.response.UpdateUserLocationResponseDTO': UpdateUserLocationResponseDTO,
    'app.whoo.data.api.response.SuggestSpotUserSpotResponse': SuggestSpotUserSpotResponse,
    'app.whoo.data.api.response.UserCheckInSpotDTO': UserCheckInSpotDTO,
    'app.whoo.data.api.response.SupportPresignedUrlsResponse': SupportPresignedUrlsResponse,
    'app.whoo.data.api.response.PlaceSearchResponse': PlaceSearchResponse,
    'app.whoo.data.api.response.RoomStreaksResponse': RoomStreaksResponse,
    'app.whoo.data.api.response.ProfileImageResponse': ProfileImageResponse,
    'app.whoo.data.api.response.StampDTO': StampDTO,
    'app.whoo.data.api.response.ComputeRoutesResponse': ComputeRoutesResponse,
    'app.whoo.data.api.response.NearbySearchLocationsResponse': NearbySearchLocationsResponse,
    'app.whoo.data.pref.StampHistoryDTO': StampHistoryDTO,
    'app.whoo.data.database.entity.MessageEntity.TextMessage': TextMessage,
    'app.whoo.data.api.request.AppleMusicTokenRequest': AppleMusicTokenRequest,
    'app.whoo.data.api.response.WhatsUpCurrentSlotStatusResponse': WhatsUpCurrentSlotStatusResponse,
}

MODEL_BY_NAME = {
    'StoredConnectedServices': StoredConnectedServices,
    'CreateUserCheckInRequest': CreateUserCheckInRequest,
    'UserSpot': UserSpot,
    'AndroidCheckInData': AndroidCheckInData,
    'EndStayRequestDTO': EndStayRequestDTO,
    'StayTimeInfo': StayTimeInfo,
    'SleepWakeupRequestDTO': SleepWakeupRequestDTO,
    'DeviceStatus': DeviceStatus,
    'UserBattery': UserBattery,
    'UserLocation': UserLocation,
    'UnlockStampSheetRequest': UnlockStampSheetRequest,
    'FriendCount': FriendCount,
    'UpdateUserCheckInRequest': UpdateUserCheckInRequest,
    'AndroidCheckInData_UpdateUserCheckInRequest': AndroidCheckInData_UpdateUserCheckInRequest,
    'UserLocationRequestDTO': UserLocationRequestDTO,
    'AppState': AppState,
    'UserBattery_UserLocationRequestDTO': UserBattery_UserLocationRequestDTO,
    'UserLocation_UserLocationRequestDTO': UserLocation_UserLocationRequestDTO,
    'ReactionDTO': ReactionDTO,
    'AddReaction': AddReaction,
    'RecommendStampSheet': RecommendStampSheet,
    'WhatsUpReplyMessageVideoResponse': WhatsUpReplyMessageVideoResponse,
    'MessageDTO': MessageDTO,
    'AddReactionText': AddReactionText,
    'WhatsUpReplyVideoDTO': WhatsUpReplyVideoDTO,
    'EventDetailDTO': EventDetailDTO,
    'StampSheet': StampSheet,
    'EventMessageDTO': EventMessageDTO,
    'Cancel': Cancel,
    'Stamp': Stamp,
    'CancelText': CancelText,
    'LinkUriInfoDTO': LinkUriInfoDTO,
    'MusicChannelPayload': MusicChannelPayload,
    'Music': Music,
    'MediaMessageDTO': MediaMessageDTO,
    'DeleteReaction': DeleteReaction,
    'ReactionDTO_ReactionListDTO': ReactionDTO_ReactionListDTO,
    'LocationDataDTO': LocationDataDTO,
    'DeleteReactionText': DeleteReactionText,
    'MediaMessageWatchLogDTO': MediaMessageWatchLogDTO,
    'NewMessage': NewMessage,
    'Text': Text,
    'MessageReadStatusDTO': MessageReadStatusDTO,
    'NewMessageText': NewMessageText,
    'StampPayload': StampPayload,
    'Data': Data,
    'ReactionDTO_MessageDTO': ReactionDTO_MessageDTO,
    'Read': Read,
    'User': User,
    'ReplyOriginalMessageDTO': ReplyOriginalMessageDTO,
    'ReadingText': ReadingText,
    'ThirdPartyServiceStatus': ThirdPartyServiceStatus,
    'StampMessageDTO': StampMessageDTO,
    'Typing': Typing,
    'UserLocationDTO': UserLocationDTO,
    'StreakInfoDTO': StreakInfoDTO,
    'BatteryDTO': BatteryDTO,
    'MessageReactionRequest': MessageReactionRequest,
    'TextMessageDTO': TextMessageDTO,
    'MessageReaction': MessageReaction,
    'SpotifyConnectStateRegisterRequest': SpotifyConnectStateRegisterRequest,
    'Capabilities': Capabilities,
    'Device': Device,
    'DeviceInfo': DeviceInfo,
    'boom': boom,
    'check_in_spot': check_in_spot,
    'comeback': comeback,
    'focus_friend_with_stamp_sheet': focus_friend_with_stamp_sheet,
    'friend_check_in': friend_check_in,
    'friend_icon_change': friend_icon_change,
    'place': place,
    'same_landmark_friend_checkin': same_landmark_friend_checkin,
    'short_video_timeline': short_video_timeline,
    'tagged_friend_checkin': tagged_friend_checkin,
    'watch_log': watch_log,
    'AppIconGetDialogParams': AppIconGetDialogParams,
    'Active': Active,
    'Expired': Expired,
    'LocationPlaceCampaignDTO': LocationPlaceCampaignDTO,
    'Route': Route,
    'FriendCheckInsResponse': FriendCheckInsResponse,
    'RecommendUserSpotDTO': RecommendUserSpotDTO,
    'AuthInfoDTO': AuthInfoDTO,
    'AuthorDTO': AuthorDTO,
    'UserSpotsDTO': UserSpotsDTO,
    'JoinRoomDTO': JoinRoomDTO,
    'ProcessData': ProcessData,
    'MemoryHighlightsLocationPlaceRankingEntryDTO': MemoryHighlightsLocationPlaceRankingEntryDTO,
    'WatchLogUser': WatchLogUser,
    'PurchaseVerificationRequest': PurchaseVerificationRequest,
    'FriendActionDTO': FriendActionDTO,
    'FriendCheckInItemDTO': FriendCheckInItemDTO,
    'RecentlyPlayedItemDTO': RecentlyPlayedItemDTO,
    'UpdateWhatsUpCaptionRequest': UpdateWhatsUpCaptionRequest,
    'SuggestUsernameRequest': SuggestUsernameRequest,
    'MessageStampListDTO': MessageStampListDTO,
    'AmazonMusicAuthState': AmazonMusicAuthState,
    'CheckinUserDTO': CheckinUserDTO,
    'MyFootprintRateResponse': MyFootprintRateResponse,
    'PremiumUserResponse': PremiumUserResponse,
    'SpotifyAccessTokenResponse': SpotifyAccessTokenResponse,
    'BoomUserDto': BoomUserDto,
    'StampMessageUserDTO': StampMessageUserDTO,
    'User_MessageEntity': User_MessageEntity,
    'WhatsUpDTO': WhatsUpDTO,
    'WhatsUpReactorsResponse': WhatsUpReactorsResponse,
    'LocationPlaceCampaignDetailDTO': LocationPlaceCampaignDetailDTO,
    'WhatsUpWithUserDTO': WhatsUpWithUserDTO,
    'RecommendUserSpotRequest': RecommendUserSpotRequest,
    'ActivateThirdPartyServicesRequest': ActivateThirdPartyServicesRequest,
    'ErrorsDTO': ErrorsDTO,
    'UserCheckInSpotsResponse': UserCheckInSpotsResponse,
    'ShouldSuggestSpotResponse': ShouldSuggestSpotResponse,
    'BannerAutoRefreshConfig': BannerAutoRefreshConfig,
    'RoomUserDTO': RoomUserDTO,
    'MemoryHighlightsLocationPlacesRankingResponseDTO': MemoryHighlightsLocationPlacesRankingResponseDTO,
    'Detail': Detail,
    'NowPlayingMusicResponse': NowPlayingMusicResponse,
    'RawLocationRecord': RawLocationRecord,
    'LocationSharingBody': LocationSharingBody,
    'Route_FriendAppealIconCropScreen': Route_FriendAppealIconCropScreen,
    'UploadFootprintUrlDTO': UploadFootprintUrlDTO,
    'SuggestUsernameResponse': SuggestUsernameResponse,
    'CheckinUsersRequest': CheckinUsersRequest,
    'MyIconRingResponse': MyIconRingResponse,
    'NearbyUserDTO': NearbyUserDTO,
    'StampMessagesDTO': StampMessagesDTO,
    'LocationPlaceCampaignsResponse': LocationPlaceCampaignsResponse,
    'ReactionListDTO': ReactionListDTO,
    'User_response': User_response,
    'user_checkin': user_checkin,
    'UserCheckInsResponse': UserCheckInsResponse,
    'PlatformLocationItemDTO': PlatformLocationItemDTO,
    'VersionControlDTO': VersionControlDTO,
    'PremiumUserSetting': PremiumUserSetting,
    'MemoryHighlightsTimeWithUsersEntryDTO': MemoryHighlightsTimeWithUsersEntryDTO,
    'FootprintDownloadStatusResponse': FootprintDownloadStatusResponse,
    'FootprintRateWorldRankingResponse': FootprintRateWorldRankingResponse,
    'EventMessage': EventMessage,
    'WhatsUpReminderConfigDTO': WhatsUpReminderConfigDTO,
    'WhatsUpStatusErrorResponse': WhatsUpStatusErrorResponse,
    'LocationSharingDTO': LocationSharingDTO,
    'UploadMediaUrlDTO': UploadMediaUrlDTO,
    'FriendDTO': FriendDTO,
    'CampaignBannerResponse': CampaignBannerResponse,
    'ActivityLogRequest': ActivityLogRequest,
    'GeocodeCenterDTO': GeocodeCenterDTO,
    'PinnedRoomRequestBody': PinnedRoomRequestBody,
    'CheckinUsersResponse': CheckinUsersResponse,
    'ThirdPartyServiceStatusDTO': ThirdPartyServiceStatusDTO,
    'RoomUsersResponse': RoomUsersResponse,
    'BoomFriendLocationsResponse': BoomFriendLocationsResponse,
    'CompletionOriginalStampRoute': CompletionOriginalStampRoute,
    'LocationPlaceDTO': LocationPlaceDTO,
    'FriendCheckInLocationDTO': FriendCheckInLocationDTO,
    'FriendsDTO': FriendsDTO,
    'UserAccount': UserAccount,
    'PlatformLocationItemResponse': PlatformLocationItemResponse,
    'BannerInfoDTO': BannerInfoDTO,
    'PremiumUserSettingsRequest': PremiumUserSettingsRequest,
    'MediaUploadRequest': MediaUploadRequest,
    'MemoryHighlightsTimeWithUsersRankingResponseDTO': MemoryHighlightsTimeWithUsersRankingResponseDTO,
    'BumpResponse': BumpResponse,
    'LinkUriInfo': LinkUriInfo,
    'WhatsUpStatusResponse': WhatsUpStatusResponse,
    'CreateSupportTicketRequest': CreateSupportTicketRequest,
    'SettingBannerResponse': SettingBannerResponse,
    'UploadOriginalStampsUrlResponse': UploadOriginalStampsUrlResponse,
    'FriendDetailDTO': FriendDetailDTO,
    'UserCheckInDetailResponse': UserCheckInDetailResponse,
    'SupportTicketDTO': SupportTicketDTO,
    'GeocodeDTO': GeocodeDTO,
    'CheckinedUserDTO': CheckinedUserDTO,
    'RoomInvitationDTO': RoomInvitationDTO,
    'RoomRequestBody': RoomRequestBody,
    'RoomWhatsupBody': RoomWhatsupBody,
    'SpotifyApresolveResponse': SpotifyApresolveResponse,
    'LegacyRecommendAdDTO': LegacyRecommendAdDTO,
    'FootprintRateDTO': FootprintRateDTO,
    'NearbyUsersDiscoveryRequest': NearbyUsersDiscoveryRequest,
    'WhatsUpMixedVideoExistsResponse': WhatsUpMixedVideoExistsResponse,
    'AuthInfoEditRoute': AuthInfoEditRoute,
    'FriendsIconRingItem': FriendsIconRingItem,
    'CampaignLocationPlaceDTO': CampaignLocationPlaceDTO,
    'MessagesDTO': MessagesDTO,
    'UserDTO': UserDTO,
    'RegisteredSpotResponse': RegisteredSpotResponse,
    'ThirdPartyServicesIntegrationStatusResponse': ThirdPartyServicesIntegrationStatusResponse,
    'Route_DeleteOriginalStampScreen': Route_DeleteOriginalStampScreen,
    'MemoryHighlightsUserDTO': MemoryHighlightsUserDTO,
    'StampSheetDTO': StampSheetDTO,
    'AppIconChangeRoute': AppIconChangeRoute,
    'Location': Location,
    'StampSheetsDTO': StampSheetsDTO,
    'Route_QrScreen': Route_QrScreen,
    'Location_request': Location_request,
    'WhatsUpRequestPostErrorResponse': WhatsUpRequestPostErrorResponse,
    'LocationPlaceMediaItemDTO': LocationPlaceMediaItemDTO,
    'FriendCheckInResponse': FriendCheckInResponse,
    'UploadProfileImageUrlDTO': UploadProfileImageUrlDTO,
    'SubscriptionGracePeriodBody': SubscriptionGracePeriodBody,
    'SupportClientContext': SupportClientContext,
    'SupportTicketResponse': SupportTicketResponse,
    'UserNavArg': UserNavArg,
    'ChangeProfileImageRequest': ChangeProfileImageRequest,
    'MarkedCheckInCheckinUserDTO': MarkedCheckInCheckinUserDTO,
    'RoomInvitationResponse': RoomInvitationResponse,
    'RoomRequestBodyFields': RoomRequestBodyFields,
    'PresignedUrlResponse': PresignedUrlResponse,
    'RoomWhatsupBodyData': RoomWhatsupBodyData,
    'NearbyUsersDiscoveryResponse': NearbyUsersDiscoveryResponse,
    'WhatsUpMyReactionDTO': WhatsUpMyReactionDTO,
    'WhatsUpTimelineResponse': WhatsUpTimelineResponse,
    'CreateWhatsUpRequest': CreateWhatsUpRequest,
    'RecommendUserSpotsResponse': RecommendUserSpotsResponse,
    'FriendsIconRingsResponse': FriendsIconRingsResponse,
    'UserDetailDTO': UserDetailDTO,
    'SavedTrack': SavedTrack,
    'SleepingFriendDto': SleepingFriendDto,
    'LegacyStampDTO': LegacyStampDTO,
    'MediaMessage': MediaMessage,
    'WhatsUpRequestPostRequest': WhatsUpRequestPostRequest,
    'UrlPathDTO': UrlPathDTO,
    'AdFeature': AdFeature,
    'SupportTicketsResponse': SupportTicketsResponse,
    'MarkedCheckInDTO': MarkedCheckInDTO,
    'DefaultReactionListDTO': DefaultReactionListDTO,
    'ReverseGeocodesResponse': ReverseGeocodesResponse,
    'RoomResponse': RoomResponse,
    'RoomWhatsupResponse': RoomWhatsupResponse,
    'BoomLocationDto': BoomLocationDto,
    'LocationDTO': LocationDTO,
    'CampaignLocationPlacesResponse': CampaignLocationPlacesResponse,
    'UserOriginalStampSheetDTO': UserOriginalStampSheetDTO,
    'Route_GhostModeScreen': Route_GhostModeScreen,
    'SleepingFriendsResponse': SleepingFriendsResponse,
    'GroupChatInviteLinkResponse': GroupChatInviteLinkResponse,
    'SpotCategoryDTO': SpotCategoryDTO,
    'LegacyStampHistoryDTO': LegacyStampHistoryDTO,
    'MediaMessageWatchLog': MediaMessageWatchLog,
    'WhatsUpRequestPostResponse': WhatsUpRequestPostResponse,
    'SubscriptionGracePeriodWatchRequest': SubscriptionGracePeriodWatchRequest,
    'FriendsLocationSharingsDTO': FriendsLocationSharingsDTO,
    'UserResponse': UserResponse,
    'DefaultStampSheetsDTO': DefaultStampSheetsDTO,
    'RoomsChannelActionDTO': RoomsChannelActionDTO,
    'RouteDTO': RouteDTO,
    'SeasonalChallengeConfig': SeasonalChallengeConfig,
    'WhatsUpOriginalMixedVideoCellDTO': WhatsUpOriginalMixedVideoCellDTO,
    'LocationPlaceMediaItemsResponse': LocationPlaceMediaItemsResponse,
    'Route_StreakDetailScreen': Route_StreakDetailScreen,
    'WhatsUpUserDTO': WhatsUpUserDTO,
    'RawMessageEventDTO': RawMessageEventDTO,
    'OriginalStampRequest': OriginalStampRequest,
    'UserHiddenDTO': UserHiddenDTO,
    'MarkedCheckInFriendDTO': MarkedCheckInFriendDTO,
    'PostMessageDTO': PostMessageDTO,
    'FootprintRatesResponse': FootprintRatesResponse,
    'WhatsUpReactionRequest': WhatsUpReactionRequest,
    'RecentlyPlayedMusicResponse': RecentlyPlayedMusicResponse,
    'SupportMessageDTO': SupportMessageDTO,
    'UserOriginalStampsDTO': UserOriginalStampsDTO,
    'RoomsDTO': RoomsDTO,
    'WhatsUp': WhatsUp,
    'WhatsUpOriginalMixedVideoDataDTO': WhatsUpOriginalMixedVideoDataDTO,
    'RandomStampResponse': RandomStampResponse,
    'UpdateLocationSharingRequest': UpdateLocationSharingRequest,
    'OriginalStampSheetDTO': OriginalStampSheetDTO,
    'FriendsYourWorldDTO': FriendsYourWorldDTO,
    'GMTDate': GMTDate,
    'UserSpotContentDTO': UserSpotContentDTO,
    'BestFriendRoute': BestFriendRoute,
    'GroupChatUserRequestBody': GroupChatUserRequestBody,
    'Time': Time,
    'BlockInformationDTO': BlockInformationDTO,
    'RoomStreakDTO': RoomStreakDTO,
    'AppIconGetRoute': AppIconGetRoute,
    'Reaction': Reaction,
    'SeasonalChallengeMissionDTO': SeasonalChallengeMissionDTO,
    'FriendRequestDTO': FriendRequestDTO,
    'WorldRankingFootprintRateDTO': WorldRankingFootprintRateDTO,
    'AuthInfoResponseDTO': AuthInfoResponseDTO,
    'SupportMessageResponse': SupportMessageResponse,
    'CheckInSpotCategoryDTO': CheckInSpotCategoryDTO,
    'RoomDTO': RoomDTO,
    'WatchCountResponse': WatchCountResponse,
    'Waypoint': Waypoint,
    'WhatsUpOriginalMixedVideoFileDTO': WhatsUpOriginalMixedVideoFileDTO,
    'WhatsUpReactionStampDTO': WhatsUpReactionStampDTO,
    'SendSupportMessageRequest': SendSupportMessageRequest,
    'SessionConfigs': SessionConfigs,
    'UpdateMarkedCheckInRequest': UpdateMarkedCheckInRequest,
    'FriendCheckInUserCheckinDTO': FriendCheckInUserCheckinDTO,
    'UserCheckInQuestionDTO': UserCheckInQuestionDTO,
    'UserSpotDTO': UserSpotDTO,
    'InviterUserDTO': InviterUserDTO,
    'MarkedCheckInFriendsResponse': MarkedCheckInFriendsResponse,
    'BillingStampDTO': BillingStampDTO,
    'MemoryHighlightsAvailabilityDTO': MemoryHighlightsAvailabilityDTO,
    'FootprintUrlDTO': FootprintUrlDTO,
    'SupportMessagesResponse': SupportMessagesResponse,
    'DefaultIconImage': DefaultIconImage,
    'CheckInSpotDTO': CheckInSpotDTO,
    'Route_RequestFriendScreen': Route_RequestFriendScreen,
    'RoomStreakDetailDTO': RoomStreakDetailDTO,
    'ReplyOriginalMessageInfo': ReplyOriginalMessageInfo,
    'WhatsUpOriginalMixedVideoResponse': WhatsUpOriginalMixedVideoResponse,
    'WhatsUpReactionStampsResponse': WhatsUpReactionStampsResponse,
    'FriendCheckInDetailDTO': FriendCheckInDetailDTO,
    'UpdateRecentlyPlayedMusicRequest': UpdateRecentlyPlayedMusicRequest,
    'FriendCheckInUserDTO': FriendCheckInUserDTO,
    'AuthUserDTO': AuthUserDTO,
    'MessageStampHistoryDTO': MessageStampHistoryDTO,
    'UserAppIconDTO': UserAppIconDTO,
    'UserCheckInQuestionsResponse': UserCheckInQuestionsResponse,
    'UserLocationsResponse': UserLocationsResponse,
    'Route_UserPageScreen': Route_UserPageScreen,
    'UserSpotResponse': UserSpotResponse,
    'PlaceSearchItemDTO': PlaceSearchItemDTO,
    'MarkedCheckInsResponse': MarkedCheckInsResponse,
    'PolylineDTO': PolylineDTO,
    'NearbyFriendRequestDTO': NearbyFriendRequestDTO,
    'MemoryHighlightsFriendRankingEntryDTO': MemoryHighlightsFriendRankingEntryDTO,
    'WatchLogItem': WatchLogItem,
    'AppIconTypeDTO': AppIconTypeDTO,
    'WhatsUpContent': WhatsUpContent,
    'AbTestAssignmentResponse': AbTestAssignmentResponse,
    'LocationNavArg': LocationNavArg,
    'SessionData': SessionData,
    'FriendShipDTO': FriendShipDTO,
    'SuggestSpotRequest': SuggestSpotRequest,
    'SupportPresignedUrlDTO': SupportPresignedUrlDTO,
    'GooglePlaceDetailsResponse': GooglePlaceDetailsResponse,
    'DefaultIconImages': DefaultIconImages,
    'CheckInSpotResponse': CheckInSpotResponse,
    'BlockUsersDTO': BlockUsersDTO,
    'StampSheetProductResponseDTO': StampSheetProductResponseDTO,
    'StampMessage': StampMessage,
    'WhatsUpPresignedUrlResponse': WhatsUpPresignedUrlResponse,
    'WhatsUpReactionSummaryDTO': WhatsUpReactionSummaryDTO,
    'LocationTriggerEventDTO': LocationTriggerEventDTO,
    'UpdateRoomRequest': UpdateRoomRequest,
    'AuthUserResponseDTO': AuthUserResponseDTO,
    'UserAppVersionRequest': UserAppVersionRequest,
    'UserCheckInResponse': UserCheckInResponse,
    'UserSpotUpdateBody': UserSpotUpdateBody,
    'FeatureFlag': FeatureFlag,
    'RequestFriendUser': RequestFriendUser,
    'OfJson': OfJson,
    'PremiumUserApiErrorResponse': PremiumUserApiErrorResponse,
    'RoomStreakResponse': RoomStreakResponse,
    'DisconnectThirdPartyServicesIntegrationRequest': DisconnectThirdPartyServicesIntegrationRequest,
    'MemoryHighlightsFriendRankingResponseDTO': MemoryHighlightsFriendRankingResponseDTO,
    'NewMessageLinkUriInfoListText': NewMessageLinkUriInfoListText,
    'SeasonalChallengeStatusResponse': SeasonalChallengeStatusResponse,
    'LocationPlacesResponse': LocationPlacesResponse,
    'SettingAboutDetailRoute': SettingAboutDetailRoute,
    'Route_IconCropScreen': Route_IconCropScreen,
    'RecommendStampSheetsDTO': RecommendStampSheetsDTO,
    'FriendShipNavArg': FriendShipNavArg,
    'SuggestSpotUserSpotDTO': SuggestSpotUserSpotDTO,
    'SupportPresignedUrlsRequest': SupportPresignedUrlsRequest,
    'MusicDTO': MusicDTO,
    'LatLngDTO': LatLngDTO,
    'ComputeRoutesRequest': ComputeRoutesRequest,
    'NearbySearchLocationDTO': NearbySearchLocationDTO,
    'StreakInfo': StreakInfo,
    'WhatsUpCreatedResponse': WhatsUpCreatedResponse,
    'WhatsUpReactionCatalogStampDTO': WhatsUpReactionCatalogStampDTO,
    'WhatsUpReactorDTO': WhatsUpReactorDTO,
    'AbTestContentDTO': AbTestContentDTO,
    'LocationTriggerEventsResponse': LocationTriggerEventsResponse,
    'UploadableUserIds': UploadableUserIds,
    'UserAppVersionResponse': UserAppVersionResponse,
    'UserSpotUpdateRequest': UserSpotUpdateRequest,
    'user_spot': user_spot,
    'PlatformLocationDetailsResponse': PlatformLocationDetailsResponse,
    'MyCurrentLocationFootprintRateResponse': MyCurrentLocationFootprintRateResponse,
    'BillingStampSheetDTO': BillingStampSheetDTO,
    'PremiumUserBody': PremiumUserBody,
    'MemoryHighlightsLocationPlaceDTO': MemoryHighlightsLocationPlaceDTO,
    'WatchLogResponse': WatchLogResponse,
    'StampMessageDTO_response': StampMessageDTO_response,
    'StampSheetProductsDTO': StampSheetProductsDTO,
    'SessionDetails': SessionDetails,
    'UpdateUserLocationResponseDTO': UpdateUserLocationResponseDTO,
    'SuggestSpotUserSpotResponse': SuggestSpotUserSpotResponse,
    'UserCheckInSpotDTO': UserCheckInSpotDTO,
    'SupportPresignedUrlsResponse': SupportPresignedUrlsResponse,
    'PlaceSearchResponse': PlaceSearchResponse,
    'RoomStreaksResponse': RoomStreaksResponse,
    'ProfileImageResponse': ProfileImageResponse,
    'StampDTO': StampDTO,
    'ComputeRoutesResponse': ComputeRoutesResponse,
    'NearbySearchLocationsResponse': NearbySearchLocationsResponse,
    'StampHistoryDTO': StampHistoryDTO,
    'TextMessage': TextMessage,
    'AppleMusicTokenRequest': AppleMusicTokenRequest,
    'WhatsUpCurrentSlotStatusResponse': WhatsUpCurrentSlotStatusResponse,
}