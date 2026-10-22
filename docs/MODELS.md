# whoo API model catalog

Total: **399** serializable models extracted from `kotlinx.serialization` descriptors.

| class | JSON keys | FQCN |
|---|---|---|
| `AbTestAssignmentResponse` | `active`, `content` | `app.whoo.data.api.response.AbTestAssignmentResponse` |
| `AbTestContentDTO` | `id`, `identifier`, `thumbnail_url`, `button_text`, `button_element_identifier`, `button_action_type` | `app.whoo.data.api.response.AbTestContentDTO` |
| `ActivateThirdPartyServicesRequest` | `service_name` | `app.whoo.data.api.request.ActivateThirdPartyServicesRequest` |
| `Active` | `roomId`, `friendProfileImage` | `app.whoo.ui.streak.StreakDetailArgs.Active` |
| `ActivityLogRequest` | `global_uuid`, `session_uuid`, `session_type`, `step`, `timestamp` | `app.whoo.data.api.request.ActivityLogRequest` |
| `AdFeature` | `width`, `height`, `delay`, `enabled`, `enabled_countries` | `app.whoo.data.api.response.AdFeature` |
| `AddReaction` | `state`, `text` | `app.whoo.data.api.response.MessageEventDTO.AddReaction` |
| `AddReactionText` | `message_id`, `stamp_id`, `stamp_url`, `message_reaction_id`, `reaction_user_id` | `app.whoo.data.api.response.MessageEventDTO.AddReaction.AddReactionText` |
| `AmazonMusicAuthState` | `accessToken`, `refreshToken`, `accessTokenExpiresAt`, `customerId`, `deviceId`, `deviceType`, `musicTerritory`, `regionPrefix`, `refreshHost`, `plan`, `tier`, `role`, `linkedMemberCount`, `lastAccountTypeRecheckAt`, `ownerWhooUserId` | `app.whoo.data.api.amazonmusic.AmazonMusicAuthState` |
| `AndroidCheckInData` | `identifier`, `latitude`, `longitude`, `category`, `name`, `address`, `phone_number` | `app.whoo.data.api.request.CreateUserCheckInRequest.AndroidCheckInData` |
| `AndroidCheckInData_UpdateUserCheckInRequest` | `identifier`, `latitude`, `longitude`, `category`, `name`, `address`, `phone_number` | `app.whoo.data.api.request.UpdateUserCheckInRequest.AndroidCheckInData` |
| `AppIconChangeRoute` | `iconType` | `app.whoo.ui.setting.AppIconChangeRoute` |
| `AppIconGetDialogParams` | `title`, `message`, `friendsText`, `daysText`, `friendTextColor`, `dayTextColor`, `iconState`, `positiveButton`, `appIconTypeId` | `app.whoo.ui.setting.AppIconGetDialogFragment.AppIconGetDialogParams` |
| `AppIconGetRoute` | `paramsJson` | `app.whoo.ui.setting.AppIconGetRoute` |
| `AppIconTypeDTO` | `id`, `icon_type`, `friends_condition`, `login_days_condition` | `app.whoo.data.api.response.AppIconTypeDTO` |
| `AppState` | `active` | `app.whoo.data.api.request.UserLocationRequestDTO.AppState` |
| `AppleMusicTokenRequest` | `access_token` | `app.whoo.data.api.request.AppleMusicTokenRequest` |
| `AuthInfoDTO` | `email`, `auth_type` | `app.whoo.data.api.response.AuthInfoDTO` |
| `AuthInfoEditRoute` | `title`, `ordinal`, `oldPassword` | `app.whoo.ui.setting.AuthInfoEditRoute` |
| `AuthInfoResponseDTO` | `auth_info` | `app.whoo.data.api.response.AuthInfoResponseDTO` |
| `AuthUserDTO` | `email` | `app.whoo.data.api.response.AuthUserDTO` |
| `AuthUserResponseDTO` | `user`, `errors` | `app.whoo.data.api.response.AuthUserResponseDTO` |
| `AuthorDTO` | `id`, `name`, `uuid` | `app.whoo.data.api.response.AuthorDTO` |
| `BannerAutoRefreshConfig` | `enabled`, `interval` | `app.whoo.data.api.response.BannerAutoRefreshConfig` |
| `BannerInfoDTO` | `display_flg`, `display_seconds`, `url`, `text` | `app.whoo.data.api.response.BannerInfoDTO` |
| `BatteryDTO` | `level`, `state` | `app.whoo.data.api.response.UserLocationsResponse.UserLocationDTO.BatteryDTO` |
| `BestFriendRoute` | `myName`, `friendName`, `myThumbUrl`, `friendThumbUrl`, `whooId` | `app.whoo.ui.mypage.BestFriendRoute` |
| `BillingStampDTO` | `id`, `image_url`, `stamp_hash`, `priority`, `file_extension` | `app.whoo.data.api.response.BillingStampDTO` |
| `BillingStampSheetDTO` | `id`, `name`, `thumbnail_image_url`, `dot_image_url`, `description`, `priority`, `expires_at`, `copyright`, `stamps`, `author` | `app.whoo.data.api.response.BillingStampSheetDTO` |
| `BlockInformationDTO` | `is_blocked`, `is_blocking` | `app.whoo.data.api.response.BlockInformationDTO` |
| `BlockUsersDTO` | `users`, `next_page` | `app.whoo.data.api.response.BlockUsersDTO` |
| `BoomFriendLocationsResponse` | `boom_users`, `gathering`, `location` | `app.whoo.data.api.response.BoomFriendLocationsResponse` |
| `BoomLocationDto` | `latitude`, `longitude` | `app.whoo.data.api.response.BoomLocationDto` |
| `BoomUserDto` | `profile_image_url` | `app.whoo.data.api.response.BoomUserDto` |
| `BumpResponse` | `users` | `app.whoo.data.api.response.BumpResponse` |
| `CampaignBannerResponse` | `location_place`, `banner_info` | `app.whoo.data.api.response.CampaignBannerResponse` |
| `CampaignLocationPlaceDTO` | `id`, `uid`, `name`, `latitude`, `longitude`, `identifier` | `app.whoo.data.api.response.CampaignLocationPlaceDTO` |
| `CampaignLocationPlacesResponse` | `location_places`, `landmark_image_url`, `next_page` | `app.whoo.data.api.response.CampaignLocationPlacesResponse` |
| `Cancel` | `text`, `state` | `app.whoo.data.api.response.MessageEventDTO.Cancel` |
| `CancelText` | `message_id` | `app.whoo.data.api.response.MessageEventDTO.Cancel.CancelText` |
| `Capabilities` | `can_be_player`, `hidden` | `app.whoo.data.api.spotify.request.SpotifyConnectStateRegisterRequest.Capabilities` |
| `ChangeProfileImageRequest` | `profile_image`, `is_appeal_friends` | `app.whoo.data.api.request.ChangeProfileImageRequest` |
| `CheckInSpotCategoryDTO` | `value`, `label` | `app.whoo.data.api.response.CheckInSpotCategoryDTO` |
| `CheckInSpotDTO` | `id`, `latitude`, `longitude`, `spot_type`, `name` | `app.whoo.data.api.response.CheckInSpotDTO` |
| `CheckInSpotResponse` | `spot` | `app.whoo.data.api.response.CheckInSpotResponse` |
| `CheckinUserDTO` | `id`, `uid`, `username`, `display_name`, `profile_image`, `spot_name` | `app.whoo.data.api.response.CheckinUserDTO` |
| `CheckinUsersRequest` | `os_info`, `identifiers` | `app.whoo.data.api.request.CheckinUsersRequest` |
| `CheckinUsersResponse` | `checkined_users` | `app.whoo.data.api.response.CheckinUsersResponse` |
| `CheckinedUserDTO` | `identifier`, `checkin_users` | `app.whoo.data.api.response.CheckinedUserDTO` |
| `CompletionOriginalStampRoute` | `capturedFiles`, `from` | `app.whoo.ui.originalstamp.CompletionOriginalStampRoute` |
| `ComputeRoutesRequest` | `origin`, `destination`, `travelMode`, `routingPreference`, `computeAlternativeRoutes` | `app.whoo.data.api.request.ComputeRoutesRequest` |
| `ComputeRoutesResponse` | `routes` | `app.whoo.data.api.response.ComputeRoutesResponse` |
| `CreateSupportTicketRequest` | `category`, `body`, `subject`, `client_context`, `fcm_token` | `app.whoo.data.api.request.CreateSupportTicketRequest` |
| `CreateUserCheckInRequest` | `android`, `name`, `user_ids` | `app.whoo.data.api.request.CreateUserCheckInRequest` |
| `CreateWhatsUpRequest` | `video_path`, `thumbnail_path`, `latitude`, `longitude`, `caption_text` | `app.whoo.data.api.request.CreateWhatsUpRequest` |
| `Data` | `id`, `priority`, `image_url`, `image_url_path`, `stamp_hash`, `stamp_sound`, `stamp_sheet_id` | `app.whoo.data.api.response.StampPayload.Data` |
| `DefaultIconImage` | `url`, `key` | `app.whoo.data.api.response.DefaultIconImage` |
| `DefaultIconImages` | `default_icon_images` | `app.whoo.data.api.response.DefaultIconImages` |
| `DefaultReactionListDTO` | `stamps` | `app.whoo.data.api.response.DefaultReactionListDTO` |
| `DefaultStampSheetsDTO` | `stamp_sheets` | `app.whoo.data.api.response.DefaultStampSheetsDTO` |
| `DeleteReaction` | `state`, `text` | `app.whoo.data.api.response.MessageEventDTO.DeleteReaction` |
| `DeleteReactionText` | `message_id`, `stamp_id`, `message_reaction_id`, `reaction_user_id` | `app.whoo.data.api.response.MessageEventDTO.DeleteReaction.DeleteReactionText` |
| `Detail` | `userId`, `displayName` | `app.whoo.data.database.entity.MessageEntity.Detail` |
| `Device` | `device_info` | `app.whoo.data.api.spotify.request.SpotifyConnectStateRegisterRequest.Device` |
| `DeviceInfo` | `capabilities` | `app.whoo.data.api.spotify.request.SpotifyConnectStateRegisterRequest.DeviceInfo` |
| `DeviceStatus` | `lock_status` | `app.whoo.data.api.request.SleepWakeupRequestDTO.DeviceStatus` |
| `DisconnectThirdPartyServicesIntegrationRequest` | `service_name`, `status` | `app.whoo.data.api.request.DisconnectThirdPartyServicesIntegrationRequest` |
| `EndStayRequestDTO` | `stay_time_info` | `app.whoo.data.api.request.EndStayRequestDTO` |
| `ErrorsDTO` | `error_code`, `errors` | `app.whoo.data.api.response.ErrorsDTO` |
| `EventDetailDTO` | `user_id`, `display_name` | `app.whoo.data.api.response.MessageDTO.EventDetailDTO` |
| `EventMessage` | `id`, `users`, `eventType`, `streakInfo` | `app.whoo.data.database.entity.MessageEntity.EventMessage` |
| `EventMessageDTO` | `id`, `event_type`, `detail`, `streak_info` | `app.whoo.data.api.response.MessageDTO.EventMessageDTO` |
| `Expired` | `friendProfileImage` | `app.whoo.ui.streak.StreakDetailArgs.Expired` |
| `FeatureFlag` | `is_background_location_enabled`, `network_location`, `ad_feature`, `is_map_camera_enabled`, `route_ui_enabled`, `use_direct_fgs_start` | `app.whoo.data.api.response.FeatureFlag` |
| `FootprintDownloadStatusResponse` | `required_refresh` | `app.whoo.data.api.response.FootprintDownloadStatusResponse` |
| `FootprintRateDTO` | `user`, `rate_percent` | `app.whoo.data.api.response.FootprintRateDTO` |
| `FootprintRateWorldRankingResponse` | `footprint_rates`, `city_polygon_name`, `next_page` | `app.whoo.data.api.response.FootprintRateWorldRankingResponse` |
| `FootprintRatesResponse` | `footprint_rates`, `city_polygon_name`, `next_page` | `app.whoo.data.api.response.FootprintRatesResponse` |
| `FootprintUrlDTO` | `urls` | `app.whoo.data.api.response.FootprintUrlDTO` |
| `FriendActionDTO` | `action_type`, `user_id` | `app.whoo.data.api.response.FriendActionDTO` |
| `FriendCheckInDetailDTO` | `latitude`, `longitude`, `spot_category`, `spot_name`, `stayed_at` | `app.whoo.data.api.response.FriendCheckInDetailDTO` |
| `FriendCheckInItemDTO` | `user_checkin`, `user` | `app.whoo.data.api.response.FriendCheckInItemDTO` |
| `FriendCheckInLocationDTO` | `identifier`, `latitude`, `longitude`, `category`, `name` | `app.whoo.data.api.response.FriendCheckInLocationDTO` |
| `FriendCheckInResponse` | `users`, `checkin`, `android` | `app.whoo.data.api.response.FriendCheckInResponse` |
| `FriendCheckInUserCheckinDTO` | `id`, `latitude`, `longitude`, `spot_category`, `spot_name`, `last_stayed_at` | `app.whoo.data.api.response.FriendCheckInUserCheckinDTO` |
| `FriendCheckInUserDTO` | `id`, `uid`, `username`, `display_name`, `profile_image` | `app.whoo.data.api.response.FriendCheckInUserDTO` |
| `FriendCheckInsResponse` | `friend_checkins`, `platform_location_item`, `next_page` | `app.whoo.data.api.response.FriendCheckInsResponse` |
| `FriendCount` | `friend_count` | `app.whoo.data.api.request.UnlockStampSheetRequest.FriendCount` |
| `FriendDTO` | `friend` | `app.whoo.data.api.response.FriendDTO` |
| `FriendDetailDTO` | `friend`, `errors` | `app.whoo.data.api.response.FriendDetailDTO` |
| `FriendRequestDTO` | `user_id`, `is_in_japan` | `app.whoo.data.api.request.FriendRequestDTO` |
| `FriendShipDTO` | `id`, `friend_id`, `user_id`, `holded_at`, `time_with`, `state`, `anniversary` | `app.whoo.data.api.response.FriendShipDTO` |
| `FriendShipNavArg` | `id`, `userId`, `state` | `app.whoo.model.FriendShipNavArg` |
| `FriendsDTO` | `friends`, `next_page` | `app.whoo.data.api.response.FriendsDTO` |
| `FriendsIconRingItem` | `icon_ring_type`, `granted_user_ids` | `app.whoo.data.api.response.FriendsIconRingItem` |
| `FriendsIconRingsResponse` | `icon_rings` | `app.whoo.data.api.response.FriendsIconRingsResponse` |
| `FriendsLocationSharingsDTO` | `ambiguous`, `freeze`, `errors` | `app.whoo.data.api.response.FriendsLocationSharingsDTO` |
| `FriendsYourWorldDTO` | `footprint_uuid`, `user_checkins` | `app.whoo.data.api.response.FriendsYourWorldDTO` |
| `GMTDate` | `seconds`, `minutes`, `hours`, `dayOfWeek`, `dayOfMonth`, `dayOfYear`, `month`, `year`, `timestamp` | `io.ktor.util.date.GMTDate` |
| `GeocodeCenterDTO` | `latitude`, `longitude` | `app.whoo.data.api.response.GeocodeCenterDTO` |
| `GeocodeDTO` | `country_name`, `city_polygon_uuid`, `polygon_url`, `city_polygon_name`, `admin_level`, `center` | `app.whoo.data.api.response.GeocodeDTO` |
| `GooglePlaceDetailsResponse` | `identifier`, `latitude`, `longitude`, `address`, `name`, `category` | `app.whoo.data.api.response.GooglePlaceDetailsResponse` |
| `GroupChatInviteLinkResponse` | `invite_link` | `app.whoo.data.api.response.GroupChatInviteLinkResponse` |
| `GroupChatUserRequestBody` | `user_ids` | `app.whoo.data.api.request.GroupChatUserRequestBody` |
| `InviterUserDTO` | `id`, `uid`, `display_name`, `username` | `app.whoo.data.api.response.InviterUserDTO` |
| `JoinRoomDTO` | `state` | `app.whoo.data.api.response.JoinRoomDTO` |
| `LatLngDTO` | `latitude`, `longitude` | `app.whoo.data.api.request.LatLngDTO` |
| `LegacyRecommendAdDTO` | `stamp_sheet_id`, `priority`, `dot_image_url`, `large_ad_image_url`, `is_once_bring_front`, `once_bring_front_cache_key` | `app.whoo.data.pref.LegacyRecommendAdDTO` |
| `LegacyStampDTO` | `id`, `priority`, `image_url`, `image_url_path`, `stamp_hash`, `stamp_sound`, `stamp_sheet_id` | `app.whoo.data.pref.LegacyStampDTO` |
| `LegacyStampHistoryDTO` | `sheetId`, `stamp`, `recommendAd` | `app.whoo.data.pref.LegacyStampHistoryDTO` |
| `LinkUriInfo` | `uri`, `title`, `favicon`, `siteName`, `description`, `thumbnailImage` | `app.whoo.data.database.entity.MessageEntity.LinkUriInfo` |
| `LinkUriInfoDTO` | `uri`, `title`, `favicon`, `site_name`, `description`, `thumbnail_image` | `app.whoo.data.api.response.MessageDTO.LinkUriInfoDTO` |
| `Location` | `latitude`, `longitude` | `app.whoo.data.database.entity.MessageEntity.Location` |
| `LocationDTO` | `latitude`, `longitude` | `app.whoo.data.api.response.LocationDTO` |
| `LocationDataDTO` | `latitude`, `longitude` | `app.whoo.data.api.response.MessageDTO.MediaMessageDTO.LocationDataDTO` |
| `LocationNavArg` | `latitude`, `longitude` | `app.whoo.model.LocationNavArg` |
| `LocationPlaceCampaignDTO` | `id`, `title`, `main_image_url`, `detail` | `app.whoo.data.api.response.LocationPlaceCampaignDTO` |
| `LocationPlaceCampaignDetailDTO` | `description`, `external_url` | `app.whoo.data.api.response.LocationPlaceCampaignDetailDTO` |
| `LocationPlaceCampaignsResponse` | `campaigns`, `landmark_image_url` | `app.whoo.data.api.response.LocationPlaceCampaignsResponse` |
| `LocationPlaceDTO` | `id`, `uid`, `name`, `latitude`, `longitude`, `identifier`, `category` | `app.whoo.data.api.response.LocationPlaceDTO` |
| `LocationPlaceMediaItemDTO` | `id`, `url`, `description`, `priority`, `thumbnail_image_url` | `app.whoo.data.api.response.LocationPlaceMediaItemDTO` |
| `LocationPlaceMediaItemsResponse` | `media_items`, `next_page` | `app.whoo.data.api.response.LocationPlaceMediaItemsResponse` |
| `LocationPlacesResponse` | `location_places`, `next_page` | `app.whoo.data.api.response.LocationPlacesResponse` |
| `LocationSharingBody` | `sharing_type`, `friend_ids`, `durations` | `app.whoo.data.api.request.LocationSharingBody` |
| `LocationSharingDTO` | `sharing_type` | `app.whoo.data.api.response.LocationSharingDTO` |
| `LocationTriggerEventDTO` | `latitude`, `longitude`, `title`, `url`, `radius_m` | `app.whoo.data.api.response.LocationTriggerEventDTO` |
| `LocationTriggerEventsResponse` | `trigger_events` | `app.whoo.data.api.response.LocationTriggerEventsResponse` |
| `Location_request` | `latLng` | `app.whoo.data.api.request.Location` |
| `MarkedCheckInCheckinUserDTO` | `profile_image` | `app.whoo.data.api.response.MarkedCheckInCheckinUserDTO` |
| `MarkedCheckInDTO` | `id`, `latitude`, `longitude`, `spot_category`, `spot_name`, `platform_location_item`, `checkin_users` | `app.whoo.data.api.response.MarkedCheckInDTO` |
| `MarkedCheckInFriendDTO` | `user`, `location_place_count` | `app.whoo.data.api.response.MarkedCheckInFriendDTO` |
| `MarkedCheckInFriendsResponse` | `friends`, `next_page` | `app.whoo.data.api.response.MarkedCheckInFriendsResponse` |
| `MarkedCheckInsResponse` | `user_checkins` | `app.whoo.data.api.response.MarkedCheckInsResponse` |
| `MediaMessage` | `id`, `uri`, `mediaType`, `mainMapMessageWatchLog`, `location`, `thumbnailImageUrl`, `messageMediaType` | `app.whoo.data.database.entity.MessageEntity.MediaMessage` |
| `MediaMessageDTO` | `id`, `media`, `send_type`, `media_type`, `thumbnail_image_url`, `media_message_watch_log`, `location` | `app.whoo.data.api.response.MessageDTO.MediaMessageDTO` |
| `MediaMessageWatchLog` | `id`, `isReading` | `app.whoo.data.database.entity.MessageEntity.MediaMessageWatchLog` |
| `MediaMessageWatchLogDTO` | `id`, `is_reading` | `app.whoo.data.api.response.MessageDTO.MediaMessageDTO.MediaMessageWatchLogDTO` |
| `MediaUploadRequest` | `media` | `app.whoo.data.api.request.MediaUploadRequest` |
| `MemoryHighlightsAvailabilityDTO` | `is_premium_user`, `month` | `app.whoo.data.api.response.MemoryHighlightsAvailabilityDTO` |
| `MemoryHighlightsFriendRankingEntryDTO` | `rank`, `user`, `count` | `app.whoo.data.api.response.MemoryHighlightsFriendRankingEntryDTO` |
| `MemoryHighlightsFriendRankingResponseDTO` | `month`, `ranking` | `app.whoo.data.api.response.MemoryHighlightsFriendRankingResponseDTO` |
| `MemoryHighlightsLocationPlaceDTO` | `id`, `name`, `address`, `emoji`, `latitude`, `longitude`, `uid` | `app.whoo.data.api.response.MemoryHighlightsLocationPlaceDTO` |
| `MemoryHighlightsLocationPlaceRankingEntryDTO` | `rank`, `location_place`, `count` | `app.whoo.data.api.response.MemoryHighlightsLocationPlaceRankingEntryDTO` |
| `MemoryHighlightsLocationPlacesRankingResponseDTO` | `month`, `ranking` | `app.whoo.data.api.response.MemoryHighlightsLocationPlacesRankingResponseDTO` |
| `MemoryHighlightsTimeWithUsersEntryDTO` | `rank`, `user`, `time_with_hours` | `app.whoo.data.api.response.MemoryHighlightsTimeWithUsersEntryDTO` |
| `MemoryHighlightsTimeWithUsersRankingResponseDTO` | `month`, `ranking` | `app.whoo.data.api.response.MemoryHighlightsTimeWithUsersRankingResponseDTO` |
| `MemoryHighlightsUserDTO` | `id`, `uid`, `display_name`, `username`, `profile_image` | `app.whoo.data.api.response.MemoryHighlightsUserDTO` |
| `MessageDTO` | `id`, `text_message`, `media_messages`, `stamp_message`, `message_type`, `event_message`, `is_reply_whatsup`, `is_whatsup_v2_reply_posted`, `uid`, `whatsup_count`, `is_watched_archived_whatsup`, `user`, `created_at`, `is_cancel`, `message_reactions`, `reply_original_message` | `app.whoo.data.api.response.MessageDTO` |
| `MessageReaction` | `stamp_id` | `app.whoo.data.api.response.MessageReactionRequest.MessageReaction` |
| `MessageReactionRequest` | `message_reaction` | `app.whoo.data.api.response.MessageReactionRequest` |
| `MessageReadStatusDTO` | `user_id`, `opened_at` | `app.whoo.data.api.response.MessageDTO.MessageReadStatusDTO` |
| `MessageStampHistoryDTO` | `stampId` | `app.whoo.data.api.response.MessageStampHistoryDTO` |
| `MessageStampListDTO` | `stamp_sheets`, `recommend_stamp_sheets` | `app.whoo.data.api.response.MessageStampListDTO` |
| `MessagesDTO` | `messages`, `next_page`, `room` | `app.whoo.data.api.response.MessagesDTO` |
| `Music` | `site_name`, `identifier`, `title`, `artist_name`, `cover_image_url`, `service_uri`, `preview_url`, `played_at`, `played_end_at`, `expected_played_end_at` | `app.whoo.data.api.response.MusicChannelPayload.Music` |
| `MusicChannelPayload` | `event`, `user_id`, `uid`, `music`, `stopped_at` | `app.whoo.data.api.response.MusicChannelPayload` |
| `MusicDTO` | `site_name`, `identifier`, `cover_image_url`, `title`, `artist_name`, `service_uri`, `played_at`, `played_end_at`, `preview_url` | `app.whoo.data.api.response.MusicDTO` |
| `MyCurrentLocationFootprintRateResponse` | `rate_percent`, `city_polygon_name` | `app.whoo.data.api.response.MyCurrentLocationFootprintRateResponse` |
| `MyFootprintRateResponse` | `rate_percent`, `city_polygon_name` | `app.whoo.data.api.response.MyFootprintRateResponse` |
| `MyIconRingResponse` | `icon_ring_type` | `app.whoo.data.api.response.MyIconRingResponse` |
| `NearbyFriendRequestDTO` | `is_in_japan` | `app.whoo.data.api.request.NearbyFriendRequestDTO` |
| `NearbySearchLocationDTO` | `identifier`, `latitude`, `longitude`, `name`, `category` | `app.whoo.data.api.response.NearbySearchLocationDTO` |
| `NearbySearchLocationsResponse` | `locations` | `app.whoo.data.api.response.NearbySearchLocationsResponse` |
| `NearbyUserDTO` | `id`, `uid`, `username`, `display_name`, `profile_image`, `introduction`, `online`, `private_mode`, `your_world_disclosure_scope` | `app.whoo.data.api.response.NearbyUserDTO` |
| `NearbyUsersDiscoveryRequest` | `latitude`, `longitude`, `unix_timestamp` | `app.whoo.data.api.request.NearbyUsersDiscoveryRequest` |
| `NearbyUsersDiscoveryResponse` | `friends`, `next_page` | `app.whoo.data.api.response.NearbyUsersDiscoveryResponse` |
| `NewMessage` | `text`, `state` | `app.whoo.data.api.response.MessageEventDTO.NewMessage` |
| `NewMessageLinkUriInfoListText` | `message_id`, `link_uri_info_list` | `app.whoo.data.api.response.MessageEventDTO.NewTextMessageLinkUriInfoList.NewMessageLinkUriInfoListText` |
| `NewMessageText` | `user_id`, `display_name`, `message`, `profile_image` | `app.whoo.data.api.response.MessageEventDTO.NewMessage.NewMessageText` |
| `NowPlayingMusicResponse` | `user_ids` | `app.whoo.data.api.response.NowPlayingMusicResponse` |
| `OfJson` | `latitude`, `longitude`, `provider`, `isBatteryCharging`, `batteryLevel`, `isNetworkEnabled`, `isLocationUpdateStaying`, `startDateOfStay`, `horizontalAccuracy`, `speed`, `bearing`, `time` | `app.whoo.model.DeviceInfo.OfJson` |
| `OriginalStampRequest` | `user_original_stamp_id`, `stamp_count`, `user_id` | `app.whoo.data.api.request.OriginalStampRequest` |
| `OriginalStampSheetDTO` | `user_original_stamp_sheet` | `app.whoo.data.api.response.OriginalStampSheetDTO` |
| `PinnedRoomRequestBody` | `room_id` | `app.whoo.data.api.request.PinnedRoomRequestBody` |
| `PlaceSearchItemDTO` | `id`, `name`, `address`, `latitude`, `longitude`, `category`, `identifier` | `app.whoo.data.api.response.PlaceSearchItemDTO` |
| `PlaceSearchResponse` | `location_places`, `next_offset` | `app.whoo.data.api.response.PlaceSearchResponse` |
| `PlatformLocationDetailsResponse` | `description`, `phone_number`, `address` | `app.whoo.data.api.response.PlatformLocationDetailsResponse` |
| `PlatformLocationItemDTO` | `platform_type`, `identifier`, `name` | `app.whoo.data.api.response.PlatformLocationItemDTO` |
| `PlatformLocationItemResponse` | `id`, `latitude`, `longitude`, `spot_category`, `spot_name`, `platform_location_item`, `tagged_users`, `last_stayed_at` | `app.whoo.data.api.response.PlatformLocationItemResponse` |
| `PolylineDTO` | `encodedPolyline` | `app.whoo.data.api.response.PolylineDTO` |
| `PostMessageDTO` | `errors` | `app.whoo.data.api.response.PostMessageDTO` |
| `PremiumUserApiErrorResponse` | `error_code` | `app.whoo.data.api.response.PremiumUserApiErrorResponse` |
| `PremiumUserBody` | `starts_at`, `expires_at`, `billing_interval`, `payment_method`, `purchase_os_type` | `app.whoo.data.api.response.PremiumUserBody` |
| `PremiumUserResponse` | `premium_user`, `subscription_grace_period` | `app.whoo.data.api.response.PremiumUserResponse` |
| `PremiumUserSetting` | `app_ui_color` | `app.whoo.data.api.request.PremiumUserSetting` |
| `PremiumUserSettingsRequest` | `premium_user_setting` | `app.whoo.data.api.request.PremiumUserSettingsRequest` |
| `PresignedUrlResponse` | `url`, `path` | `app.whoo.location.telemetry.upload.PresignedUrlResponse` |
| `ProcessData` | `pid`, `uuid` | `com.google.firebase.sessions.ProcessData` |
| `ProfileImageResponse` | `profile_image` | `app.whoo.data.api.response.ProfileImageResponse` |
| `PurchaseVerificationRequest` | `purchase_token`, `product_id` | `app.whoo.data.api.request.PurchaseVerificationRequest` |
| `RandomStampResponse` | `image_url` | `app.whoo.data.api.response.RandomStampResponse` |
| `RawLocationRecord` | `latitude`, `longitude`, `horizontalAccuracy`, `altitude`, `velocity`, `bearing`, `time`, `state`, `isForeground`, `charging`, `batteryLevel`, `expired`, `valid`, `provider`, `isWifiConnected`, `enablePost`, `significantMotionTriggered`, `hasSpeed`, `hasSpeedAccuracy`, `speedAccuracyMetersPerSecond`, `isJumped`, `locationModelVariant`, `jumpScore`, `consecutiveJumpCount`, `jumpInputDistance`, `stayedAt` | `app.whoo.location.telemetry.spool.RawLocationRecord` |
| `RawMessageEventDTO` | `state`, `text` | `app.whoo.data.api.response.RawMessageEventDTO` |
| `Reaction` | `reactionId`, `stampId`, `userId`, `imageUrl` | `app.whoo.data.database.entity.MessageEntity.Reaction` |
| `ReactionDTO` | `id`, `image_url` | `app.whoo.data.api.response.DefaultReactionListDTO.ReactionDTO` |
| `ReactionDTO_MessageDTO` | `id`, `user_id`, `stamp_id`, `image_url`, `stamp_sheet_id` | `app.whoo.data.api.response.MessageDTO.ReactionDTO` |
| `ReactionDTO_ReactionListDTO` | `id`, `priority`, `image_url`, `category` | `app.whoo.data.api.response.ReactionListDTO.ReactionDTO` |
| `ReactionListDTO` | `stamps` | `app.whoo.data.api.response.ReactionListDTO` |
| `Read` | `text`, `state` | `app.whoo.data.api.response.MessageEventDTO.Read` |
| `ReadingText` | `user_id`, `opened_at` | `app.whoo.data.api.response.MessageEventDTO.Read.ReadingText` |
| `RecentlyPlayedItemDTO` | `music`, `user` | `app.whoo.data.api.response.RecentlyPlayedItemDTO` |
| `RecentlyPlayedMusicResponse` | `recently_played`, `thirdparty_service`, `next_page` | `app.whoo.data.api.response.RecentlyPlayedMusicResponse` |
| `RecommendStampSheet` | `stamp_sheet_id`, `priority`, `dot_image_url`, `large_ad_image_url` | `app.whoo.data.api.response.MessageStampListDTO.RecommendStampSheet` |
| `RecommendStampSheetsDTO` | `stamp_sheet_id`, `priority`, `dot_image_url`, `large_ad_image_url`, `is_once_bring_front`, `once_bring_front_cache_key` | `app.whoo.data.api.response.RecommendStampSheetsDTO` |
| `RecommendUserSpotDTO` | `id`, `latitude`, `longitude`, `radius_meter` | `app.whoo.data.api.response.RecommendUserSpotDTO` |
| `RecommendUserSpotRequest` | `spot_type`, `latitude`, `longitude` | `app.whoo.data.api.request.RecommendUserSpotRequest` |
| `RecommendUserSpotsResponse` | `recommend_user_spots`, `next_page` | `app.whoo.data.api.response.RecommendUserSpotsResponse` |
| `RegisteredSpotResponse` | `id`, `latitude`, `longitude`, `spot_category`, `spot_name` | `app.whoo.data.api.response.RegisteredSpotResponse` |
| `ReplyOriginalMessageDTO` | `id`, `text_message`, `media_messages`, `stamp_message`, `message_type`, `is_reply_whatsup`, `uid`, `user`, `is_cancel` | `app.whoo.data.api.response.MessageDTO.ReplyOriginalMessageDTO` |
| `ReplyOriginalMessageInfo` | `id`, `uid`, `isCancel`, `messageType`, `isReplyWhatsup`, `textMessage`, `mediaMessage`, `stampMessage`, `user` | `app.whoo.data.database.entity.MessageEntity.ReplyOriginalMessageInfo` |
| `RequestFriendUser` | `id`, `displayName`, `profileImage`, `friendState` | `app.whoo.ui.addfriend.RequestFriendUser` |
| `ReverseGeocodesResponse` | `geocodes` | `app.whoo.data.api.response.ReverseGeocodesResponse` |
| `RoomDTO` | `id`, `last_message`, `messaged_at`, `uid`, `unreading_message_count`, `user_states`, `state`, `users`, `room_type`, `name`, `icon_image`, `pinned_at`, `join_room_state`, `sort_timestamp` | `app.whoo.data.api.response.RoomDTO` |
| `RoomInvitationDTO` | `id`, `uid`, `name`, `icon_image`, `state`, `join_room_state`, `users`, `inviter_user` | `app.whoo.data.api.response.RoomInvitationDTO` |
| `RoomInvitationResponse` | `room`, `inviter_user`, `error_code`, `room_id` | `app.whoo.data.api.response.RoomInvitationResponse` |
| `RoomRequestBody` | `room` | `app.whoo.data.api.request.RoomRequestBody` |
| `RoomRequestBodyFields` | `name`, `icon_image`, `add_user_ids`, `remove_user_ids`, `uid` | `app.whoo.data.api.request.RoomRequestBodyFields` |
| `RoomResponse` | `room`, `errors` | `app.whoo.data.api.response.RoomResponse` |
| `RoomStreakDTO` | `room_id`, `count`, `streak_state`, `badge` | `app.whoo.data.api.response.RoomStreakDTO` |
| `RoomStreakDetailDTO` | `count`, `streak_state`, `badge`, `freeze_starts_at`, `freeze_ends_at` | `app.whoo.data.api.response.RoomStreakDetailDTO` |
| `RoomStreakResponse` | `streak` | `app.whoo.data.api.response.RoomStreakResponse` |
| `RoomStreaksResponse` | `streaks` | `app.whoo.data.api.response.RoomStreaksResponse` |
| `RoomUserDTO` | `id`, `username`, `display_name`, `profile_image`, `friendship`, `join_room`, `friend_count` | `app.whoo.data.api.response.RoomUserDTO` |
| `RoomUsersResponse` | `users`, `next_page` | `app.whoo.data.api.response.RoomUsersResponse` |
| `RoomWhatsupBody` | `message` | `app.whoo.data.api.request.RoomWhatsupBody` |
| `RoomWhatsupBodyData` | `uid` | `app.whoo.data.api.request.RoomWhatsupBodyData` |
| `RoomWhatsupResponse` | `message`, `errors` | `app.whoo.data.api.response.RoomWhatsupResponse` |
| `RoomsChannelActionDTO` | `state`, `text` | `app.whoo.data.api.response.RoomsChannelActionDTO` |
| `RoomsDTO` | `rooms` | `app.whoo.data.api.response.RoomsDTO` |
| `Route` | `from` | `app.whoo.ui.originalstamp.CreateOriginalStampScreen.Route` |
| `RouteDTO` | `distanceMeters`, `duration`, `polyline` | `app.whoo.data.api.response.RouteDTO` |
| `Route_DeleteOriginalStampScreen` | `stampId`, `stampUrl` | `app.whoo.ui.originalstamp.DeleteOriginalStampScreen.Route` |
| `Route_FriendAppealIconCropScreen` | `image` | `app.whoo.ui.setting.FriendAppealIconCropScreen.Route` |
| `Route_GhostModeScreen` | `userId`, `displayName`, `profileImage` | `app.whoo.ui.ghostmode.GhostModeScreen.Route` |
| `Route_IconCropScreen` | `image` | `app.whoo.ui.setting.IconCropScreen.Route` |
| `Route_QrScreen` | `screenMode`, `from` | `app.whoo.ui.qr.QrScreen.Route` |
| `Route_RequestFriendScreen` | `userJson`, `fromShake` | `app.whoo.ui.addfriend.RequestFriendScreen.Route` |
| `Route_StreakDetailScreen` | `argsJson` | `app.whoo.ui.streak.StreakDetailScreen.Route` |
| `Route_UserPageScreen` | `userId`, `previousUserId` | `app.whoo.ui.userpage.UserPageScreen.Route` |
| `SavedTrack` | `asin`, `isPaused`, `durationSec`, `sentAtEpochMs` | `app.whoo.data.api.amazonmusic.AmazonMusicLastSentTrackLocalDataSource.SavedTrack` |
| `SeasonalChallengeConfig` | `name`, `is_enabled` | `app.whoo.data.api.response.SeasonalChallengeConfig` |
| `SeasonalChallengeMissionDTO` | `mission_type`, `completed`, `current_count`, `required_count`, `needs_animation` | `app.whoo.data.api.response.SeasonalChallengeMissionDTO` |
| `SeasonalChallengeStatusResponse` | `challenge_period`, `missions` | `app.whoo.data.api.response.SeasonalChallengeStatusResponse` |
| `SendSupportMessageRequest` | `kind`, `body`, `media`, `thumbnail`, `fcm_token` | `app.whoo.data.api.request.SendSupportMessageRequest` |
| `SessionConfigs` | `sessionsEnabled`, `sessionSamplingRate`, `sessionTimeoutSeconds`, `cacheDurationSeconds`, `cacheUpdatedTimeSeconds` | `com.google.firebase.sessions.settings.SessionConfigs` |
| `SessionData` | `sessionDetails`, `backgroundTime`, `processDataMap` | `com.google.firebase.sessions.SessionData` |
| `SessionDetails` | `sessionId`, `firstSessionId`, `sessionIndex`, `sessionStartTimestampUs` | `com.google.firebase.sessions.SessionDetails` |
| `SettingAboutDetailRoute` | `ordinal` | `app.whoo.ui.setting.SettingAboutDetailRoute` |
| `SettingBannerResponse` | `banner_type`, `banner_image_url` | `app.whoo.data.api.response.SettingBannerResponse` |
| `ShouldSuggestSpotResponse` | `should_suggest` | `app.whoo.data.api.response.ShouldSuggestSpotResponse` |
| `SleepWakeupRequestDTO` | `user_location`, `user_battery`, `device_status` | `app.whoo.data.api.request.SleepWakeupRequestDTO` |
| `SleepingFriendDto` | `user_id`, `start_sleep_at` | `app.whoo.data.api.response.SleepingFriendDto` |
| `SleepingFriendsResponse` | `friends` | `app.whoo.data.api.response.SleepingFriendsResponse` |
| `SpotCategoryDTO` | `value`, `label` | `app.whoo.data.api.response.SpotCategoryDTO` |
| `SpotifyAccessTokenResponse` | `accessToken`, `accessTokenExpirationTimestampMs`, `isAnonymous` | `app.whoo.data.api.spotify.response.SpotifyAccessTokenResponse` |
| `SpotifyApresolveResponse` | `dealer-g2`, `spclient` | `app.whoo.data.api.spotify.response.SpotifyApresolveResponse` |
| `SpotifyConnectStateRegisterRequest` | `member_type`, `device` | `app.whoo.data.api.spotify.request.SpotifyConnectStateRegisterRequest` |
| `Stamp` | `id`, `priority`, `stamp_hash`, `image_url` | `app.whoo.data.api.response.MessageStampListDTO.StampSheet.Stamp` |
| `StampDTO` | `id`, `priority`, `image_url`, `image_url_path`, `stamp_hash`, `stamp_sound`, `stamp_sheet_id` | `app.whoo.data.api.response.StampDTO` |
| `StampHistoryDTO` | `sheet_id`, `stamp_id`, `is_recommend_ad` | `app.whoo.data.pref.StampHistoryDTO` |
| `StampMessage` | `id`, `stampSheetId`, `imageUrl`, `stampHash` | `app.whoo.data.database.entity.MessageEntity.StampMessage` |
| `StampMessageDTO` | `id`, `stamp_sheet_id`, `image_url`, `stamp_hash` | `app.whoo.data.api.response.MessageDTO.StampMessageDTO` |
| `StampMessageDTO_response` | `user`, `sender`, `stamp`, `stamp_count`, `created_at` | `app.whoo.data.api.response.StampMessageDTO` |
| `StampMessageUserDTO` | `id` | `app.whoo.data.api.response.StampMessageUserDTO` |
| `StampMessagesDTO` | `stamp_messages` | `app.whoo.data.api.response.StampMessagesDTO` |
| `StampPayload` | `user`, `sender`, `stamp`, `stamp_count` | `app.whoo.data.api.response.StampPayload` |
| `StampSheet` | `id`, `name`, `priority`, `thumbnail_image_url`, `stamps` | `app.whoo.data.api.response.MessageStampListDTO.StampSheet` |
| `StampSheetDTO` | `id`, `name`, `priority`, `is_display_whatsup`, `stamps` | `app.whoo.data.api.response.StampSheetDTO` |
| `StampSheetProductResponseDTO` | `stamp_sheet_products`, `next_page` | `app.whoo.data.api.response.StampSheetProductResponseDTO` |
| `StampSheetProductsDTO` | `id`, `identifier`, `is_free`, `is_japan_only`, `is_purchased`, `is_purchasable`, `stamp_sheet` | `app.whoo.data.api.response.StampSheetProductsDTO` |
| `StampSheetsDTO` | `stamp_sheets`, `recommend_stamp_sheets`, `unlock_friend_count_conditions` | `app.whoo.data.api.response.StampSheetsDTO` |
| `StayTimeInfo` | `latitude`, `longitude`, `horizontal_accuracy`, `stayed_at`, `updated_at` | `app.whoo.data.api.request.EndStayRequestDTO.StayTimeInfo` |
| `StoredConnectedServices` | `ownerWhooUserId`, `services` | `app.whoo.data.api.ConnectedServicesLocalDataSource.StoredConnectedServices` |
| `StreakInfo` | `streakCount`, `badge`, `freezeStartsAt`, `freezeEndsAt`, `isLinkActive` | `app.whoo.data.database.entity.MessageEntity.StreakInfo` |
| `StreakInfoDTO` | `streak_count`, `badge`, `freeze_starts_at`, `freeze_ends_at`, `is_link_active` | `app.whoo.data.api.response.MessageDTO.StreakInfoDTO` |
| `SubscriptionGracePeriodBody` | `expires_at`, `show_modal`, `modal_type` | `app.whoo.data.api.response.SubscriptionGracePeriodBody` |
| `SubscriptionGracePeriodWatchRequest` | `modal_type` | `app.whoo.data.api.request.SubscriptionGracePeriodWatchRequest` |
| `SuggestSpotRequest` | `spot_type`, `latitude`, `longitude` | `app.whoo.data.api.request.SuggestSpotRequest` |
| `SuggestSpotUserSpotDTO` | `id`, `latitude`, `longitude`, `spot_type` | `app.whoo.data.api.response.SuggestSpotUserSpotDTO` |
| `SuggestSpotUserSpotResponse` | `user_spot` | `app.whoo.data.api.response.SuggestSpotUserSpotResponse` |
| `SuggestUsernameRequest` | `display_name` | `app.whoo.data.api.request.SuggestUsernameRequest` |
| `SuggestUsernameResponse` | `username` | `app.whoo.data.api.response.SuggestUsernameResponse` |
| `SupportClientContext` | `app_version`, `os_version`, `device_model`, `locale` | `app.whoo.data.api.request.SupportClientContext` |
| `SupportMessageDTO` | `id`, `sender`, `kind`, `body`, `media_url`, `thumbnail_url`, `created_at` | `app.whoo.data.api.response.SupportMessageDTO` |
| `SupportMessageResponse` | `message` | `app.whoo.data.api.response.SupportMessageResponse` |
| `SupportMessagesResponse` | `messages` | `app.whoo.data.api.response.SupportMessagesResponse` |
| `SupportPresignedUrlDTO` | `file_name`, `url`, `path` | `app.whoo.data.api.response.SupportPresignedUrlDTO` |
| `SupportPresignedUrlsRequest` | `filenames` | `app.whoo.data.api.request.SupportPresignedUrlsRequest` |
| `SupportPresignedUrlsResponse` | `urls` | `app.whoo.data.api.response.SupportPresignedUrlsResponse` |
| `SupportTicketDTO` | `id`, `category`, `subject`, `status`, `unread_by_user`, `last_activity_at`, `created_at` | `app.whoo.data.api.response.SupportTicketDTO` |
| `SupportTicketResponse` | `ticket` | `app.whoo.data.api.response.SupportTicketResponse` |
| `SupportTicketsResponse` | `tickets` | `app.whoo.data.api.response.SupportTicketsResponse` |
| `Text` | `room_id`, `unread_count` | `app.whoo.data.api.response.RoomsChannelActionDTO.Text` |
| `TextMessage` | `id`, `body`, `linkUriInfoList` | `app.whoo.data.database.entity.MessageEntity.TextMessage` |
| `TextMessageDTO` | `id`, `body`, `link_uri_info_list` | `app.whoo.data.api.response.MessageDTO.TextMessageDTO` |
| `ThirdPartyServiceStatus` | `service_category_type`, `service_name`, `status` | `app.whoo.data.api.response.ThirdPartyServicesIntegrationStatusResponse.ThirdPartyServiceStatus` |
| `ThirdPartyServiceStatusDTO` | `status`, `service_name` | `app.whoo.data.api.response.ThirdPartyServiceStatusDTO` |
| `ThirdPartyServicesIntegrationStatusResponse` | `thirdparty_services` | `app.whoo.data.api.response.ThirdPartyServicesIntegrationStatusResponse` |
| `Time` | `ms`, `us`, `seconds` | `com.google.firebase.sessions.Time` |
| `Typing` | `action`, `text`, `state`, `uid` | `app.whoo.data.api.response.MessageEventDTO.Typing` |
| `UnlockStampSheetRequest` | `stamp_sheet` | `app.whoo.data.api.request.UnlockStampSheetRequest` |
| `UpdateLocationSharingRequest` | `location_sharing` | `app.whoo.data.api.request.UpdateLocationSharingRequest` |
| `UpdateMarkedCheckInRequest` | `spot_name`, `user_ids` | `app.whoo.data.api.request.UpdateMarkedCheckInRequest` |
| `UpdateRecentlyPlayedMusicRequest` | `service_name`, `identifier`, `title`, `artist_name`, `cover_image_url`, `service_uri`, `duration_sec`, `is_paused`, `preview_url` | `app.whoo.data.api.request.UpdateRecentlyPlayedMusicRequest` |
| `UpdateRoomRequest` | `icon_image` | `app.whoo.data.api.request.UpdateRoomRequest` |
| `UpdateUserCheckInRequest` | `android`, `name`, `user_ids` | `app.whoo.data.api.request.UpdateUserCheckInRequest` |
| `UpdateUserLocationResponseDTO` | `updating` | `app.whoo.data.api.response.UpdateUserLocationResponseDTO` |
| `UpdateWhatsUpCaptionRequest` | `caption_text` | `app.whoo.data.api.request.UpdateWhatsUpCaptionRequest` |
| `UploadFootprintUrlDTO` | `url` | `app.whoo.data.api.response.UploadFootprintUrlDTO` |
| `UploadMediaUrlDTO` | `urls` | `app.whoo.data.api.response.UploadMediaUrlDTO` |
| `UploadOriginalStampsUrlResponse` | `url`, `path` | `app.whoo.data.api.response.UploadOriginalStampsUrlResponse` |
| `UploadProfileImageUrlDTO` | `original`, `thumbnail` | `app.whoo.data.api.response.UploadProfileImageUrlDTO` |
| `UploadableUserIds` | `ids` | `app.whoo.data.api.response.UploadableUserIds` |
| `UrlPathDTO` | `url`, `path` | `app.whoo.data.api.response.UrlPathDTO` |
| `User` | `id` | `app.whoo.data.api.response.StampPayload.User` |
| `UserAccount` | `display_name`, `profile_image`, `birthday`, `username`, `email`, `password`, `referrership_uid`, `adid` | `app.whoo.data.api.request.UserAccount` |
| `UserAppIconDTO` | `id`, `app_icon`, `icon_state`, `check_conditions` | `app.whoo.data.api.response.UserAppIconDTO` |
| `UserAppVersionRequest` | `app_version` | `app.whoo.data.api.request.UserAppVersionRequest` |
| `UserAppVersionResponse` | `app_version` | `app.whoo.data.api.response.UserAppVersionResponse` |
| `UserBattery` | `level`, `state` | `app.whoo.data.api.request.SleepWakeupRequestDTO.UserBattery` |
| `UserBattery_UserLocationRequestDTO` | `level`, `state` | `app.whoo.data.api.request.UserLocationRequestDTO.UserBattery` |
| `UserCheckInDetailResponse` | `id`, `latitude`, `longitude`, `spot_category`, `spot_name`, `address`, `stayed_at`, `left_at`, `stay_time_minute`, `notify_identifier`, `platform_location_item` | `app.whoo.data.api.response.UserCheckInDetailResponse` |
| `UserCheckInQuestionDTO` | `id`, `latitude`, `longitude`, `horizontal_accuracy`, `is_friend_registered`, `is_today_checkin` | `app.whoo.data.api.response.UserCheckInQuestionDTO` |
| `UserCheckInQuestionsResponse` | `user_checkins`, `next_page` | `app.whoo.data.api.response.UserCheckInQuestionsResponse` |
| `UserCheckInResponse` | `user_checkin` | `app.whoo.data.api.response.UserCheckInResponse` |
| `UserCheckInSpotDTO` | `id`, `latitude`, `longitude`, `spot_category`, `spot_name`, `checkin_count`, `spot_address`, `platform_location_item` | `app.whoo.data.api.response.UserCheckInSpotDTO` |
| `UserCheckInSpotsResponse` | `user_checkins`, `next_page` | `app.whoo.data.api.response.UserCheckInSpotsResponse` |
| `UserCheckInsResponse` | `user_checkins` | `app.whoo.data.api.response.UserCheckInsResponse` |
| `UserDTO` | `id`, `uid`, `username`, `display_name`, `footprint_uuid`, `profile_image`, `introduction`, `online`, `login_days`, `max_login_days`, `created_at`, `block_information`, `friendship`, `watch_count`, `watch_user_count`, `pop_points`, `friend_count`, `time_with`, `birthday`, `your_world_disclosure_scope`, `private_mode`, `allow_recommended_users`, `user_app_icons`, `location`, `world_rank`, `user_type`, `whoo_supporter`, `location_sharing`, `whatsup_count`, `bump_count` | `app.whoo.data.api.response.UserDTO` |
| `UserDetailDTO` | `friends`, `user`, `next_page`, `mutual_total_count`, `total_count` | `app.whoo.data.api.response.UserDetailDTO` |
| `UserHiddenDTO` | `hidden_user_ids`, `errors` | `app.whoo.data.api.response.UserHiddenDTO` |
| `UserLocation` | `latitude`, `longitude`, `speed`, `stayed_at`, `bearing`, `horizontal_accuracy`, `getting_location_type` | `app.whoo.data.api.request.SleepWakeupRequestDTO.UserLocation` |
| `UserLocationDTO` | `user`, `battery`, `latitude`, `longitude`, `stayed_at`, `speed`, `sharing_type`, `updated_at`, `horizontal_accuracy`, `bearing` | `app.whoo.data.api.response.UserLocationsResponse.UserLocationDTO` |
| `UserLocationRequestDTO` | `user_location`, `user_battery`, `app_state`, `user_spot` | `app.whoo.data.api.request.UserLocationRequestDTO` |
| `UserLocation_UserLocationRequestDTO` | `latitude`, `longitude`, `speed`, `stayed_at`, `bearing`, `horizontal_accuracy`, `getting_location_type` | `app.whoo.data.api.request.UserLocationRequestDTO.UserLocation` |
| `UserLocationsResponse` | `locations` | `app.whoo.data.api.response.UserLocationsResponse` |
| `UserNavArg` | `id`, `displayName`, `profileImage`, `location`, `friendship` | `app.whoo.model.UserNavArg` |
| `UserOriginalStampSheetDTO` | `id`, `uuid`, `thumbnail_image_url`, `is_display_whatsup`, `user_original_stamps`, `max_stamp_count` | `app.whoo.data.api.response.UserOriginalStampSheetDTO` |
| `UserOriginalStampsDTO` | `id`, `stamp_sound`, `priority`, `image_url` | `app.whoo.data.api.response.UserOriginalStampsDTO` |
| `UserResponse` | `user`, `access_token`, `errors` | `app.whoo.data.api.response.UserResponse` |
| `UserSpot` | `id` | `app.whoo.data.api.request.UserLocationRequestDTO.UserSpot` |
| `UserSpotContentDTO` | `id`, `latitude`, `longitude`, `name`, `spot_type`, `user_checkin_id` | `app.whoo.data.api.response.UserSpotContentDTO` |
| `UserSpotDTO` | `id`, `latitude`, `longitude`, `name`, `spot_type`, `user_checkin_id` | `app.whoo.data.api.response.UserSpotDTO` |
| `UserSpotResponse` | `spot` | `app.whoo.data.api.response.UserSpotResponse` |
| `UserSpotUpdateBody` | `latitude`, `longitude`, `spot_type`, `name` | `app.whoo.data.api.response.UserSpotUpdateBody` |
| `UserSpotUpdateRequest` | `user_spot` | `app.whoo.data.api.response.UserSpotUpdateRequest` |
| `UserSpotsDTO` | `spots` | `app.whoo.data.api.response.UserSpotsDTO` |
| `User_MessageEntity` | `id`, `uid`, `displayName`, `profileImageUrl` | `app.whoo.data.database.entity.MessageEntity.User` |
| `User_response` | `id`, `display_name`, `username`, `profile_image` | `app.whoo.data.api.response.User` |
| `VersionControlDTO` | `minimum_support_version`, `recommend_version`, `update_url` | `app.whoo.data.api.response.VersionControlDTO` |
| `WatchCountResponse` | `watch_count`, `profile_images`, `is_enable_premium` | `app.whoo.data.api.response.WatchCountResponse` |
| `WatchLogItem` | `user`, `watch_count`, `watched_at` | `app.whoo.data.api.response.WatchLogItem` |
| `WatchLogResponse` | `total_count`, `watch_logs`, `next_page` | `app.whoo.data.api.response.WatchLogResponse` |
| `WatchLogUser` | `id`, `uid`, `display_name`, `username`, `profile_image` | `app.whoo.data.api.response.WatchLogUser` |
| `Waypoint` | `location` | `app.whoo.data.api.request.Waypoint` |
| `WhatsUp` | `whatsup` | `app.whoo.data.api.WhatsUp` |
| `WhatsUpContent` | `id`, `media`, `media_type`, `thumbnail_image_url` | `app.whoo.data.api.WhatsUpContent` |
| `WhatsUpCreatedResponse` | `whatsup_video` | `app.whoo.data.api.response.WhatsUpCreatedResponse` |
| `WhatsUpCurrentSlotStatusResponse` | `unread_count`, `slot_ends_at` | `app.whoo.data.api.response.WhatsUpCurrentSlotStatusResponse` |
| `WhatsUpDTO` | `id`, `video_url`, `posted_slot_at`, `latitude`, `longitude`, `created_at` | `app.whoo.data.api.response.WhatsUpDTO` |
| `WhatsUpMixedVideoExistsResponse` | `exists` | `app.whoo.data.api.response.WhatsUpMixedVideoExistsResponse` |
| `WhatsUpMyReactionDTO` | `stamp` | `app.whoo.data.api.response.WhatsUpMyReactionDTO` |
| `WhatsUpOriginalMixedVideoCellDTO` | `user_id`, `row`, `col`, `caption_text` | `app.whoo.data.api.response.WhatsUpOriginalMixedVideoCellDTO` |
| `WhatsUpOriginalMixedVideoDataDTO` | `files` | `app.whoo.data.api.response.WhatsUpOriginalMixedVideoDataDTO` |
| `WhatsUpOriginalMixedVideoFileDTO` | `video_url`, `thumbnail_url`, `position` | `app.whoo.data.api.response.WhatsUpOriginalMixedVideoFileDTO` |
| `WhatsUpOriginalMixedVideoResponse` | `whatsup_original_mixed_video` | `app.whoo.data.api.response.WhatsUpOriginalMixedVideoResponse` |
| `WhatsUpPresignedUrlResponse` | `url`, `path`, `thumbnail_url`, `thumbnail_path`, `max_video_seconds` | `app.whoo.data.api.response.WhatsUpPresignedUrlResponse` |
| `WhatsUpReactionCatalogStampDTO` | `id`, `priority`, `image_url`, `category` | `app.whoo.data.api.response.WhatsUpReactionCatalogStampDTO` |
| `WhatsUpReactionRequest` | `stamp_id` | `app.whoo.data.api.request.WhatsUpReactionRequest` |
| `WhatsUpReactionStampDTO` | `id`, `image_url` | `app.whoo.data.api.response.WhatsUpReactionStampDTO` |
| `WhatsUpReactionStampsResponse` | `stamps` | `app.whoo.data.api.response.WhatsUpReactionStampsResponse` |
| `WhatsUpReactionSummaryDTO` | `stamp`, `reaction_count` | `app.whoo.data.api.response.WhatsUpReactionSummaryDTO` |
| `WhatsUpReactorDTO` | `stamp`, `user` | `app.whoo.data.api.response.WhatsUpReactorDTO` |
| `WhatsUpReactorsResponse` | `reaction_stamps`, `next_page` | `app.whoo.data.api.response.WhatsUpReactorsResponse` |
| `WhatsUpReminderConfigDTO` | `enabled`, `start_hour`, `end_hour` | `app.whoo.data.featureflag.WhatsUpReminderConfigDTO` |
| `WhatsUpReplyMessageVideoResponse` | `whatsup_video` | `app.whoo.data.api.response.WhatsUpReplyMessageVideoResponse` |
| `WhatsUpReplyVideoDTO` | `id`, `video_url`, `thumbnail_url`, `posted_slot_at` | `app.whoo.data.api.response.WhatsUpReplyMessageVideoResponse.WhatsUpReplyVideoDTO` |
| `WhatsUpRequestPostErrorResponse` | `code` | `app.whoo.data.api.response.WhatsUpRequestPostErrorResponse` |
| `WhatsUpRequestPostRequest` | `user_id` | `app.whoo.data.api.request.WhatsUpRequestPostRequest` |
| `WhatsUpRequestPostResponse` | `status` | `app.whoo.data.api.response.WhatsUpRequestPostResponse` |
| `WhatsUpStatusErrorResponse` | `code` | `app.whoo.data.api.response.WhatsUpStatusErrorResponse` |
| `WhatsUpStatusResponse` | `slot_at`, `status` | `app.whoo.data.api.response.WhatsUpStatusResponse` |
| `WhatsUpTimelineResponse` | `whatsup_videos`, `next_page` | `app.whoo.data.api.response.WhatsUpTimelineResponse` |
| `WhatsUpUserDTO` | `id`, `uid`, `display_name`, `username`, `profile_image` | `app.whoo.data.api.response.WhatsUpUserDTO` |
| `WhatsUpWithUserDTO` | `id`, `video_url`, `thumbnail_url`, `posted_slot_at`, `latitude`, `longitude`, `created_at`, `user`, `caption_text`, `reaction_summaries`, `my_reaction` | `app.whoo.data.api.response.WhatsUpWithUserDTO` |
| `WorldRankingFootprintRateDTO` | `user`, `rank`, `rate_percent` | `app.whoo.data.api.response.WorldRankingFootprintRateDTO` |
| `boom` | `friendId`, `timestamp`, `notificationId`, `boomSummaryId` | `boom` |
| `check_in_spot` | `userCheckInId`, `spotName`, `latitude`, `longitude`, `timestamp`, `notificationId` | `check_in_spot` |
| `comeback` | `friendId`, `timestamp`, `notificationId` | `comeback` |
| `focus_friend_with_stamp_sheet` | `friendId`, `timestamp`, `notificationId` | `focus_friend_with_stamp_sheet` |
| `friend_check_in` | `userCheckInId`, `friendCheckInId`, `timestamp`, `notificationId` | `friend_check_in` |
| `friend_icon_change` | `friendId`, `iconUrl`, `stampId`, `timestamp`, `notificationId` | `friend_icon_change` |
| `place` | `latitude`, `longitude`, `timestamp`, `notificationId` | `place` |
| `same_landmark_friend_checkin` | `identifier`, `latitude`, `longitude`, `timestamp`, `notificationId`, `notificationDeliveryId`, `userId` | `same_landmark_friend_checkin` |
| `short_video_timeline` | `timestamp`, `notificationId`, `slotAt`, `postId` | `short_video_timeline` |
| `tagged_friend_checkin` | `identifier`, `latitude`, `longitude`, `timestamp`, `notificationId` | `tagged_friend_checkin` |
| `user_checkin` | `id`, `spot_name`, `latitude`, `longitude`, `spot_category`, `checkin_count`, `stay_checkin_count`, `is_myspot_recommend`, `user_spot` | `user_checkin` |
| `user_spot` | `id`, `spot_type` | `user_spot` |
| `watch_log` | `timestamp`, `notificationId` | `watch_log` |
