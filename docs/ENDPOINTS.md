# whoo API endpoint catalog

Total: **213** endpoints (GET 115, POST 58, PUT 2, DELETE 17, PATCH 21)

| method | path | path params | query params | body | response | auth |
|---|---|---|---|---|---|---|
| `GET` | `ab_test/assignment` | - | - | - | AbTestAssignmentResponse | yes |
| `POST` | `ab_test/content/{id}/watch` | id | - | - | - | yes |
| `POST` | `activity_logs` | - | - | ActivityLogRequest | - | yes |
| `GET` | `android/raw_locations/presigned_url` | - | - | - | UrlPathDTO | yes |
| `GET` | `api/token` | - | reason, productType, totp, totpServer, totpVer | - | SpotifyAccessTokenResponse | no |
| `GET` | `auth_info` | - | - | - | AuthInfoResponseDTO | yes |
| `GET` | `aws/s3/footprint/presigned_url` | - | filename | - | UploadFootprintUrlDTO | yes |
| `GET` | `campaigns/banner` | - | - | - | CampaignBannerResponse | yes |
| `GET` | `campaigns/location_places/nearby` | - | latitude, longitude, page, per | - | CampaignLocationPlacesResponse | yes |
| `GET` | `checkins` | - | - | - | UserCheckInsResponse | yes |
| `DELETE` | `checkins/{checkin_id}` | checkin_id | - | - | UserCheckInDTO | yes |
| `POST` | `checkins/{checkin_id}/spots` | checkin_id | - | multipart | CheckInSpotResponse | yes |
| `GET` | `checkins/{id}` | id | - | - | UserCheckInResponse | yes |
| `POST` | `directions/v2:computeRoutes` | - | - | ComputeRoutesRequest | ComputeRoutesResponse | no |
| `POST` | `email/login` | - | - | multipart | UserResponse | no |
| `PATCH` | `email/user` | - | - | multipart | AuthUserResponseDTO | yes |
| `POST` | `email/users` | - | - | UserAccount | UserResponse | no |
| `GET` | `embed/track/{trackId}` | trackId | - | - | fk9 | yes |
| `GET` | `footprint/download_status` | - | - | - | FootprintDownloadStatusResponse | yes |
| `POST` | `footprint/download_status/failed` | - | - | - | - | yes |
| `POST` | `footprint/download_status/success` | - | - | - | - | yes |
| `POST` | `footprint/upload/complete` | - | - | - | - | yes |
| `GET` | `footprint_rates` | - | country_name, uuid, page | - | FootprintRatesResponse | yes |
| `GET` | `footprint_rates/my` | - | country_name, uuid | - | MyFootprintRateResponse | yes |
| `GET` | `footprint_rates/my/current_location` | - | - | - | MyCurrentLocationFootprintRateResponse | yes |
| `GET` | `footprint_rates/world_ranking` | - | country_name, uuid, page | - | FootprintRateWorldRankingResponse | yes |
| `PUT` | `friend/location_sharing` | - | - | UpdateLocationSharingRequest | FriendsLocationSharingsDTO | yes |
| `GET` | `friend/location_sharings` | - | - | - | FriendsLocationSharingsDTO | yes |
| `GET` | `friends` | - | sort, filter, display_name | - | FriendsDTO | yes |
| `POST` | `friends` | - | - | multipart | FriendDTO | yes |
| `POST` | `friends` | - | - | FriendRequestDTO | FriendDetailDTO | yes |
| `GET` | `friends/best` | - | - | - | FriendsDTO | yes |
| `GET` | `friends/recommend` | - | page | - | FriendsDTO | yes |
| `GET` | `friends/requested` | - | - | - | FriendsDTO | yes |
| `GET` | `friends/search` | - | display_name | - | FriendsDTO | yes |
| `DELETE` | `friends/{id}` | id | - | - | - | yes |
| `GET` | `friends/{id}/yourworlds` | id | - | - | FriendsYourWorldDTO | yes |
| `GET` | `friendships/list` | - | state, page, per | - | FriendsDTO | yes |
| `PATCH` | `friendships/{id}/hold` | id | - | - | - | yes |
| `DELETE` | `friendships/{id}/retire` | id | - | - | - | yes |
| `GET` | `google/place_details/{identifier}` | identifier | dryrun | - | GooglePlaceDetailsResponse | yes |
| `GET` | `location/trigger_events` | - | - | - | LocationTriggerEventsResponse | yes |
| `GET` | `location_places/nearby` | - | latitude, longitude, radius_km, page, per | - | LocationPlacesResponse | yes |
| `GET` | `location_places/search` | - | query, latitude, longitude, offset | - | PlaceSearchResponse | yes |
| `GET` | `location_places/{location_place_id}/campaigns` | location_place_id | - | - | LocationPlaceCampaignsResponse | yes |
| `GET` | `location_places/{location_place_id}/media_items` | location_place_id | page, per | - | LocationPlaceMediaItemsResponse | yes |
| `GET` | `locations` | - | - | - | UserLocationsResponse | yes |
| `GET` | `maintenance` | - | - | - | ErrorsDTO | yes |
| `PATCH` | `media_message_watch_logs/{id}` | id | - | - | - | yes |
| `GET` | `memory_highlights/availability` | - | - | - | MemoryHighlightsAvailabilityDTO | yes |
| `DELETE` | `messages/{id}` | id | - | - | - | yes |
| `POST` | `messages/{messageId}/message_reactions` | messageId | - | MessageReactionRequest | - | yes |
| `DELETE` | `messages/{messageId}/message_reactions/{reactionId}` | messageId, reactionId | - | - | - | yes |
| `GET` | `my` | - | - | - | UserResponse | yes |
| `GET` | `nearby/users/discoveries` | - | - | - | NearbyUsersDiscoveryResponse | yes |
| `POST` | `nearby/users/discoveries` | - | - | NearbyUsersDiscoveryRequest | - | yes |
| `POST` | `nearby/users/discoveries/{user_id}/friend_request` | user_id | - | NearbyFriendRequestDTO | - | yes |
| `POST` | `nearby/users/discoveries/{user_id}/friend_request/reject` | user_id | - | - | - | yes |
| `PATCH` | `password/change` | - | - | multipart | ErrorsDTO | yes |
| `POST` | `password/forget` | - | - | - | ErrorsDTO | no |
| `GET` | `platform_locations/details/{identifier}` | identifier | latitude, longitude, name, address | - | PlatformLocationDetailsResponse | yes |
| `GET` | `recommend_user_spots` | - | page | - | RecommendUserSpotsResponse | yes |
| `DELETE` | `recommend_user_spots/{id}` | id | - | - | - | yes |
| `POST` | `recommend_user_spots/{id}/user_spots` | id | - | RecommendUserSpotRequest | SuggestSpotUserSpotResponse | yes |
| `GET` | `reverse_geocodes` | - | latitude, longitude | - | ReverseGeocodesResponse | yes |
| `GET` | `room/invite_link` | - | code | - | RoomInvitationResponse | yes |
| `POST` | `room/invite_link` | - | room_id | - | GroupChatInviteLinkResponse | yes |
| `POST` | `room/invite_link/approve` | - | code | - | - | yes |
| `GET` | `rooms` | - | limit | - | RoomsDTO | yes |
| `GET` | `rooms` | - | limit, name, last_room_id, include_all_states | - | RoomsDTO | yes |
| `GET` | `rooms` | - | name, last_room_id, limit | - | RoomsDTO | yes |
| `GET` | `rooms` | - | name, limit | - | RoomsDTO | yes |
| `GET` | `rooms` | - | last_room_id, limit | - | RoomsDTO | yes |
| `POST` | `rooms` | - | - | RoomRequestBody | RoomResponse | yes |
| `GET` | `rooms/default_icon_images` | - | - | - | DefaultIconImages | yes |
| `POST` | `rooms/pinned_rooms` | - | - | PinnedRoomRequestBody | RoomResponse | yes |
| `DELETE` | `rooms/pinned_rooms/{id}` | id | - | - | - | yes |
| `GET` | `rooms/streaks` | - | - | - | RoomStreaksResponse | yes |
| `DELETE` | `rooms/{id}` | id | - | - | - | yes |
| `PATCH` | `rooms/{id}` | id | - | RoomRequestBody | RoomResponse | yes |
| `PATCH` | `rooms/{id}` | id | - | UpdateRoomRequest | - | yes |
| `PATCH` | `rooms/{id}/hide` | id | - | - | - | yes |
| `GET` | `rooms/{id}/invitation` | id | - | - | RoomInvitationDTO | yes |
| `GET` | `rooms/{id}/locations` | id | - | - | UserLocationsResponse | yes |
| `GET` | `rooms/{id}/messages` | id | page | - | MessagesDTO | yes |
| `POST` | `rooms/{id}/messages` | id | - | multipart | PostMessageDTO | yes |
| `DELETE` | `rooms/{id}/users` | id | - | - | - | yes |
| `GET` | `rooms/{id}/users` | id | page, state | - | RoomUsersResponse | yes |
| `POST` | `rooms/{id}/users/add` | id | - | GroupChatUserRequestBody | - | yes |
| `POST` | `rooms/{id}/users/approve` | id | - | - | - | yes |
| `DELETE` | `rooms/{id}/users/delete` | id | user_ids[] | - | - | yes |
| `POST` | `rooms/{id}/users/reject` | id | - | - | - | yes |
| `POST` | `rooms/{id}/whatsups` | id | - | RoomWhatsupBody | RoomWhatsupResponse | yes |
| `GET` | `rooms/{room_id}/presigned_url` | room_id | filenames[] | - | UploadMediaUrlDTO | yes |
| `GET` | `rooms/{room_id}/streak` | room_id | - | - | RoomStreakResponse | yes |
| `GET` | `seasonal_challenges/friends/icon_rings` | - | - | - | FriendsIconRingsResponse | yes |
| `GET` | `seasonal_challenges/icon_rings/me` | - | - | - | MyIconRingResponse | yes |
| `GET` | `seasonal_challenges/{challenge_code}/status` | challenge_code | is_in_japan | - | SeasonalChallengeStatusResponse | yes |
| `POST` | `sleep_time` | - | - | SleepWakeupRequestDTO | - | yes |
| `GET` | `sleep_time/friends` | - | - | - | SleepingFriendsResponse | yes |
| `GET` | `stamp_messages` | - | - | - | StampMessagesDTO | yes |
| `POST` | `stamp_messages` | - | - | multipart | - | yes |
| `GET` | `stamp_sheet_products` | - | page | - | StampSheetProductResponseDTO | yes |
| `GET` | `stamp_sheet_products` | - | page, type | - | StampSheetProductResponseDTO | yes |
| `GET` | `stamps/default_reaction_stamps` | - | - | - | DefaultReactionListDTO | yes |
| `GET` | `stamps/reaction_stamps` | - | keywords | - | ReactionListDTO | yes |
| `GET` | `stamps/{id}` | id | - | - | RandomStampResponse | yes |
| `GET` | `support/tickets` | - | - | - | SupportTicketsResponse | yes |
| `POST` | `support/tickets` | - | - | CreateSupportTicketRequest | SupportTicketResponse | yes |
| `GET` | `support/tickets/{id}/messages` | id | after_id | - | SupportMessagesResponse | yes |
| `POST` | `support/tickets/{id}/messages` | id | - | SendSupportMessageRequest | SupportMessageResponse | yes |
| `POST` | `support/tickets/{id}/presigned_urls` | id | - | SupportPresignedUrlsRequest | SupportPresignedUrlsResponse | yes |
| `POST` | `support/tickets/{id}/read` | id | - | - | - | yes |
| `POST` | `support/tickets/{id}/resolve` | id | - | - | - | yes |
| `GET` | `thirdparty_services` | - | - | - | ThirdPartyServicesIntegrationStatusResponse | yes |
| `POST` | `thirdparty_services/activate` | - | - | ActivateThirdPartyServicesRequest | - | yes |
| `POST` | `thirdparty_services/apple_music/token` | - | - | AppleMusicTokenRequest | - | yes |
| `PATCH` | `thirdparty_services/status` | - | - | DisconnectThirdPartyServicesIntegrationRequest | - | yes |
| `DELETE` | `user` | - | - | - | - | yes |
| `PATCH` | `user` | - | - | multipart | UserResponse | yes |
| `PUT` | `user/app_icons/{id}` | id | - | - | - | yes |
| `GET` | `user/app_versions` | - | - | - | UserAppVersionResponse | yes |
| `PATCH` | `user/app_versions` | - | - | UserAppVersionRequest | - | yes |
| `GET` | `user/boom_friend_locations/{bump_summary_id}` | bump_summary_id | - | - | BoomFriendLocationsResponse | yes |
| `GET` | `user/bump` | - | - | - | BumpResponse | yes |
| `POST` | `user/bump` | - | - | multipart | - | yes |
| `PATCH` | `user/location` | - | - | UserLocationRequestDTO | UpdateUserLocationResponseDTO | yes |
| `POST` | `user/location/end_stay` | - | - | EndStayRequestDTO | - | yes |
| `DELETE` | `user/logout` | - | - | - | - | yes |
| `GET` | `user/music/now_playing` | - | - | - | NowPlayingMusicResponse | yes |
| `GET` | `user/music/recently_played` | - | page, user_id | - | RecentlyPlayedMusicResponse | yes |
| `PATCH` | `user/music/recently_played` | - | - | UpdateRecentlyPlayedMusicRequest | - | yes |
| `POST` | `user/music/recently_played/stop` | - | - | - | - | yes |
| `PATCH` | `user/offline` | - | - | multipart | - | yes |
| `PATCH` | `user/offline` | - | - | - | - | yes |
| `PATCH` | `user/online` | - | - | - | - | yes |
| `POST` | `user/original_stamp_messages` | - | - | OriginalStampRequest | - | yes |
| `GET` | `user/original_stamp_sheets` | - | - | - | OriginalStampSheetDTO | yes |
| `POST` | `user/original_stamps` | - | - | MediaUploadRequest | - | yes |
| `GET` | `user/original_stamps/presigned_url` | - | cached_content_index.exi | - | UploadOriginalStampsUrlResponse | yes |
| `DELETE` | `user/original_stamps/{id}` | id | - | - | - | yes |
| `PATCH` | `user/profile_images` | - | - | ChangeProfileImageRequest | ProfileImageResponse | yes |
| `GET` | `user/profile_images/presigned_url` | - | filename | - | UploadProfileImageUrlDTO | yes |
| `GET` | `user/setting_banner` | - | is_in_japan | - | SettingBannerResponse | yes |
| `GET` | `user/spots` | - | - | - | UserSpotsDTO | yes |
| `DELETE` | `user/spots/{id}` | id | - | - | - | yes |
| `PATCH` | `user/spots/{id}` | id | - | UserSpotUpdateRequest | UserSpotResponse | yes |
| `GET` | `user_blocks` | - | page | - | BlockUsersDTO | yes |
| `POST` | `user_checkin_push_notification_deliveries/{id}/open` | id | - | - | - | yes |
| `GET` | `user_checkins/marked_checkins` | - | user_id, exclude_user_ids | - | MarkedCheckInsResponse | yes |
| `GET` | `user_checkins/marked_checkins/friends` | - | page | - | MarkedCheckInFriendsResponse | yes |
| `PATCH` | `user_checkins/marked_checkins/{id}` | id | - | UpdateMarkedCheckInRequest | - | yes |
| `POST` | `user_checkins/{id}/suggest_spots/user_spots` | id | - | SuggestSpotRequest | SuggestSpotUserSpotResponse | yes |
| `POST` | `username/suggest` | - | - | SuggestUsernameRequest | SuggestUsernameResponse | yes |
| `POST` | `users/{id}/block` | id | - | - | - | yes |
| `DELETE` | `users/{id}/block_release` | id | - | - | - | yes |
| `POST` | `users/{id}/hidden` | id | - | - | UserHiddenDTO | yes |
| `GET` | `users/{id}/leaderboard` | id | - | - | FriendsDTO | yes |
| `GET` | `users/{id}/pops` | id | page, per | - | FriendsDTO | yes |
| `GET` | `users/{id}/room` | id | - | - | MessagesDTO | yes |
| `GET` | `users/{user_id}/footprints` | user_id | - | - | FootprintUrlDTO | yes |
| `GET` | `users/{user_name}/username` | user_name | - | - | UserDetailDTO | yes |
| `GET` | `v2/rooms/{id}` | id | - | - | RoomResponse | yes |
| `GET` | `v2/stamp_sheets` | - | - | - | DefaultStampSheetsDTO | yes |
| `GET` | `v2/stamp_sheets/room_stamp_sheets` | - | - | - | MessageStampListDTO | yes |
| `POST` | `v2/stamp_sheets/unlock` | - | - | UnlockStampSheetRequest | - | yes |
| `GET` | `v2/stamp_sheets/unlocked_stamp_sheets` | - | - | - | StampSheetsDTO | yes |
| `POST` | `v2/user_checkins` | - | - | CreateUserCheckInRequest | RegisteredSpotResponse | yes |
| `POST` | `v2/user_checkins/checkin_users` | - | - | CheckinUsersRequest | CheckinUsersResponse | yes |
| `GET` | `v2/user_checkins/platform_location_items/{identifier}` | identifier | - | - | PlatformLocationItemResponse | yes |
| `GET` | `v2/user_checkins/platform_location_items/{identifier}/friend_checkins` | identifier | page | - | FriendCheckInsResponse | yes |
| `GET` | `v2/user_checkins/questions` | - | page | - | UserCheckInQuestionsResponse | yes |
| `GET` | `v2/user_checkins/spots` | - | page | - | UserCheckInSpotsResponse | yes |
| `GET` | `v2/user_checkins/{id}` | id | from | - | UserCheckInDetailResponse | yes |
| `PATCH` | `v2/user_checkins/{id}` | id | - | UpdateUserCheckInRequest | RegisteredSpotResponse | yes |
| `GET` | `v2/user_checkins/{id}/friend_checkin` | id | friend_checkin_id | - | FriendCheckInResponse | yes |
| `GET` | `v2/user_checkins/{id}/nearby_search_locations` | id | - | - | NearbySearchLocationsResponse | yes |
| `GET` | `v2/user_checkins/{id}/should_suggest_spot` | id | - | - | ShouldSuggestSpotResponse | yes |
| `GET` | `v2/users/{id}` | id | - | - | UserDetailDTO | yes |
| `GET` | `v2/users/{id}` | id | page | - | FriendsDTO | yes |
| `GET` | `v2/watch_log/watch_count` | - | - | - | WatchCountResponse | yes |
| `GET` | `v2/watch_log/watched_by` | - | period, page, per | - | WatchLogResponse | yes |
| `GET` | `v2/watch_log/watching` | - | page, per | - | WatchLogResponse | yes |
| `GET` | `v2/whatsup/mixed_video/exists` | - | - | - | WhatsUpMixedVideoExistsResponse | yes |
| `POST` | `v2/whatsup/mixed_video/request_backend` | - | - | - | - | yes |
| `GET` | `v2/whatsup/original_mixed_video` | - | slot_at | - | WhatsUpOriginalMixedVideoResponse | yes |
| `POST` | `v2/whatsup/request_post` | - | - | WhatsUpRequestPostRequest | WhatsUpRequestPostResponse | yes |
| `POST` | `v2/whatsup/rooms/{room_id}/request_posts` | room_id | - | - | WhatsUpRequestPostResponse | yes |
| `POST` | `v2/whatsup_video` | - | - | CreateWhatsUpRequest | WhatsUpCreatedResponse | yes |
| `GET` | `v2/whatsup_video/current_slot_status` | - | - | - | WhatsUpCurrentSlotStatusResponse | yes |
| `GET` | `v2/whatsup_video/messages/{message_id}` | message_id | - | - | WhatsUpReplyMessageVideoResponse | yes |
| `GET` | `v2/whatsup_video/presigned_url` | - | - | - | WhatsUpPresignedUrlResponse | yes |
| `GET` | `v2/whatsup_video/reaction_stamps` | - | - | - | WhatsUpReactionStampsResponse | yes |
| `GET` | `v2/whatsup_video/timeline` | - | page, per | - | WhatsUpTimelineResponse | yes |
| `GET` | `v2/whatsup_video/users/{user_id}/status` | user_id | - | - | WhatsUpStatusResponse | yes |
| `DELETE` | `v2/whatsup_video/{id}` | id | - | - | - | yes |
| `PATCH` | `v2/whatsup_video/{id}` | id | - | UpdateWhatsUpCaptionRequest | - | yes |
| `DELETE` | `v2/whatsup_video/{id}/reaction` | id | - | - | - | yes |
| `POST` | `v2/whatsup_video/{id}/reaction` | id | - | WhatsUpReactionRequest | - | yes |
| `GET` | `v2/whatsup_video/{id}/reactions` | id | page | - | WhatsUpReactorsResponse | yes |
| `POST` | `validate/email` | - | - | - | ErrorsDTO | no |
| `POST` | `validate/username` | - | - | - | ErrorsDTO | no |
| `POST` | `wakeup_time` | - | - | SleepWakeupRequestDTO | - | yes |
| `POST` | `whoo_premium/android/premium_users` | - | - | PurchaseVerificationRequest | PremiumUserResponse | yes |
| `GET` | `whoo_premium/memory_highlights/location_places` | - | - | - | MemoryHighlightsLocationPlacesRankingResponseDTO | yes |
| `GET` | `whoo_premium/memory_highlights/time_with_count_friends` | - | - | - | MemoryHighlightsFriendRankingResponseDTO | yes |
| `GET` | `whoo_premium/memory_highlights/time_with_users` | - | - | - | MemoryHighlightsTimeWithUsersRankingResponseDTO | yes |
| `GET` | `whoo_premium/memory_highlights/watched_by` | - | - | - | MemoryHighlightsFriendRankingResponseDTO | yes |
| `GET` | `whoo_premium/memory_highlights/watching` | - | - | - | MemoryHighlightsFriendRankingResponseDTO | yes |
| `GET` | `whoo_premium/messages/{messageId}/whatsup` | messageId | - | - | WhatsUp | yes |
| `PATCH` | `whoo_premium/premium_user_settings` | - | - | PremiumUserSettingsRequest | - | yes |
| `GET` | `whoo_premium/v2/premium_user` | - | - | - | PremiumUserResponse | yes |
| `POST` | `whoo_premium/v2/subscription_grace_period/watch` | - | - | SubscriptionGracePeriodWatchRequest | - | yes |

## Base URL overrides

Most endpoints use `https://www.wh00.ooo/api/`. Two interfaces in the APK use a
different Retrofit base URL and are marked accordingly:

| interface | base URL | endpoints |
|---|---|---|
| `gqa` | `https://open.spotify.com/` | `GET api/token` |
| `bg4` | `https://routes.googleapis.com/` | `GET directions/v2:computeRoutes` |
