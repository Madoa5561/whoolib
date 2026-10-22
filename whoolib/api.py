"""Generated API method wrappers (do not edit by hand).

Each method maps 1:1 to a Retrofit endpoint found in the whoo APK.
Arguments use the wire-level parameter names; see ``docs/ENDPOINTS.md``.
"""

from __future__ import annotations

from typing import Any, Mapping, Optional


class API:
    """Facade over :class:`whoolib.client.WhooClient` with one method per endpoint."""

    def __init__(self, client: "WhooClient"):
        self._client = client


    def delete_checkins_checkin_id(self, checkin_id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE checkins/{checkin_id}

        Params: checkin_id
        Response: UserCheckInDTO
        Auth: required
        """
        return self._client.call('delete_checkins_checkin_id',
            path={'checkin_id': checkin_id},
            headers=headers,
        )

    def delete_friends_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE friends/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_friends_id',
            path={'id': id},
            headers=headers,
        )

    def delete_friendships_id_retire(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE friendships/{id}/retire

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_friendships_id_retire',
            path={'id': id},
            headers=headers,
        )

    def delete_messages_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE messages/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_messages_id',
            path={'id': id},
            headers=headers,
        )

    def delete_messages_message_id_message_reactions_reaction_id(self, messageId, reactionId, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE messages/{messageId}/message_reactions/{reactionId}

        Params: messageId, reactionId
        Response: empty
        Auth: required
        """
        return self._client.call('delete_messages_message_id_message_reactions_reaction_id',
            path={'messageId': messageId, 'reactionId': reactionId},
            headers=headers,
        )

    def delete_recommend_user_spots_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE recommend_user_spots/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_recommend_user_spots_id',
            path={'id': id},
            headers=headers,
        )

    def delete_rooms_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE rooms/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_rooms_id',
            path={'id': id},
            headers=headers,
        )

    def delete_rooms_id_users(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE rooms/{id}/users

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_rooms_id_users',
            path={'id': id},
            headers=headers,
        )

    def delete_rooms_id_users_delete(self, id, *, user_ids: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE rooms/{id}/users/delete

        Params: id, user_ids[]
        Response: empty
        Auth: required
        """
        return self._client.call('delete_rooms_id_users_delete',
            path={'id': id},
            query={'user_ids[]': user_ids},
            headers=headers,
        )

    def delete_rooms_pinned_rooms_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE rooms/pinned_rooms/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_rooms_pinned_rooms_id',
            path={'id': id},
            headers=headers,
        )

    def delete_user(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE user
        Response: empty
        Auth: required
        """
        return self._client.call('delete_user',
            headers=headers,
        )

    def delete_user_logout(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE user/logout
        Response: empty
        Auth: required
        """
        return self._client.call('delete_user_logout',
            headers=headers,
        )

    def delete_user_original_stamps_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE user/original_stamps/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_user_original_stamps_id',
            path={'id': id},
            headers=headers,
        )

    def delete_user_spots_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE user/spots/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_user_spots_id',
            path={'id': id},
            headers=headers,
        )

    def delete_users_id_block_release(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE users/{id}/block_release

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_users_id_block_release',
            path={'id': id},
            headers=headers,
        )

    def delete_v2_whatsup_video_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE v2/whatsup_video/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_v2_whatsup_video_id',
            path={'id': id},
            headers=headers,
        )

    def delete_v2_whatsup_video_id_reaction(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """DELETE v2/whatsup_video/{id}/reaction

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('delete_v2_whatsup_video_id_reaction',
            path={'id': id},
            headers=headers,
        )

    def get_ab_test_assignment(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET ab_test/assignment
        Response: AbTestAssignmentResponse
        Auth: required
        """
        return self._client.call('get_ab_test_assignment',
            headers=headers,
        )

    def get_android_raw_locations_presigned_url(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET android/raw_locations/presigned_url
        Response: UrlPathDTO
        Auth: required
        """
        return self._client.call('get_android_raw_locations_presigned_url',
            headers=headers,
        )

    def get_api_token(self, *, reason: Any = None, productType: Any = None, totp: Any = None, totpServer: Any = None, totpVer: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET api/token

        Params: reason, productType, totp, totpServer, totpVer
        Response: SpotifyAccessTokenResponse
        Auth: not required
        """
        return self._client.call('get_api_token',
            query={'reason': reason, 'productType': productType, 'totp': totp, 'totpServer': totpServer, 'totpVer': totpVer},
            headers=headers,
        )

    def get_auth_info(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET auth_info
        Response: AuthInfoResponseDTO
        Auth: required
        """
        return self._client.call('get_auth_info',
            headers=headers,
        )

    def get_aws_s3_footprint_presigned_url(self, *, filename: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET aws/s3/footprint/presigned_url

        Params: filename
        Response: UploadFootprintUrlDTO
        Auth: required
        """
        return self._client.call('get_aws_s3_footprint_presigned_url',
            query={'filename': filename},
            headers=headers,
        )

    def get_campaigns_banner(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET campaigns/banner
        Response: CampaignBannerResponse
        Auth: required
        """
        return self._client.call('get_campaigns_banner',
            headers=headers,
        )

    def get_campaigns_location_places_nearby(self, *, latitude: Any = None, longitude: Any = None, page: Any = None, per: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET campaigns/location_places/nearby

        Params: latitude, longitude, page, per
        Response: CampaignLocationPlacesResponse
        Auth: required
        """
        return self._client.call('get_campaigns_location_places_nearby',
            query={'latitude': latitude, 'longitude': longitude, 'page': page, 'per': per},
            headers=headers,
        )

    def get_checkins(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET checkins
        Response: UserCheckInsResponse
        Auth: required
        """
        return self._client.call('get_checkins',
            headers=headers,
        )

    def get_checkins_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET checkins/{id}

        Params: id
        Response: UserCheckInResponse
        Auth: required
        """
        return self._client.call('get_checkins_id',
            path={'id': id},
            headers=headers,
        )

    def get_embed_track_track_id(self, trackId, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET embed/track/{trackId}

        Params: trackId
        Response: fk9
        Auth: required
        """
        return self._client.call('get_embed_track_track_id',
            path={'trackId': trackId},
            headers=headers,
        )

    def get_footprint_download_status(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET footprint/download_status
        Response: FootprintDownloadStatusResponse
        Auth: required
        """
        return self._client.call('get_footprint_download_status',
            headers=headers,
        )

    def get_footprint_rates(self, *, country_name: Any = None, uuid: Any = None, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET footprint_rates

        Params: country_name, uuid, page
        Response: FootprintRatesResponse
        Auth: required
        """
        return self._client.call('get_footprint_rates',
            query={'country_name': country_name, 'uuid': uuid, 'page': page},
            headers=headers,
        )

    def get_footprint_rates_my(self, *, country_name: Any = None, uuid: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET footprint_rates/my

        Params: country_name, uuid
        Response: MyFootprintRateResponse
        Auth: required
        """
        return self._client.call('get_footprint_rates_my',
            query={'country_name': country_name, 'uuid': uuid},
            headers=headers,
        )

    def get_footprint_rates_my_current_location(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET footprint_rates/my/current_location
        Response: MyCurrentLocationFootprintRateResponse
        Auth: required
        """
        return self._client.call('get_footprint_rates_my_current_location',
            headers=headers,
        )

    def get_footprint_rates_world_ranking(self, *, country_name: Any = None, uuid: Any = None, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET footprint_rates/world_ranking

        Params: country_name, uuid, page
        Response: FootprintRateWorldRankingResponse
        Auth: required
        """
        return self._client.call('get_footprint_rates_world_ranking',
            query={'country_name': country_name, 'uuid': uuid, 'page': page},
            headers=headers,
        )

    def get_friend_location_sharings(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET friend/location_sharings
        Response: FriendsLocationSharingsDTO
        Auth: required
        """
        return self._client.call('get_friend_location_sharings',
            headers=headers,
        )

    def get_friends(self, *, sort: Any = None, filter: Any = None, display_name: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET friends

        Params: sort, filter, display_name
        Response: FriendsDTO
        Auth: required
        """
        return self._client.call('get_friends',
            query={'sort': sort, 'filter': filter, 'display_name': display_name},
            headers=headers,
        )

    def get_friends_best(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET friends/best
        Response: FriendsDTO
        Auth: required
        """
        return self._client.call('get_friends_best',
            headers=headers,
        )

    def get_friends_id_yourworlds(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET friends/{id}/yourworlds

        Params: id
        Response: FriendsYourWorldDTO
        Auth: required
        """
        return self._client.call('get_friends_id_yourworlds',
            path={'id': id},
            headers=headers,
        )

    def get_friends_recommend(self, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET friends/recommend

        Params: page
        Response: FriendsDTO
        Auth: required
        """
        return self._client.call('get_friends_recommend',
            query={'page': page},
            headers=headers,
        )

    def get_friends_requested(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET friends/requested
        Response: FriendsDTO
        Auth: required
        """
        return self._client.call('get_friends_requested',
            headers=headers,
        )

    def get_friends_search(self, *, display_name: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET friends/search

        Params: display_name
        Response: FriendsDTO
        Auth: required
        """
        return self._client.call('get_friends_search',
            query={'display_name': display_name},
            headers=headers,
        )

    def get_friendships_list(self, *, state: Any = None, page: Any = None, per: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET friendships/list

        Params: state, page, per
        Response: FriendsDTO
        Auth: required
        """
        return self._client.call('get_friendships_list',
            query={'state': state, 'page': page, 'per': per},
            headers=headers,
        )

    def get_google_place_details_identifier(self, identifier, *, dryrun: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET google/place_details/{identifier}

        Params: identifier, dryrun
        Response: GooglePlaceDetailsResponse
        Auth: required
        """
        return self._client.call('get_google_place_details_identifier',
            path={'identifier': identifier},
            query={'dryrun': dryrun},
            headers=headers,
        )

    def get_location_places_location_place_id_campaigns(self, location_place_id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET location_places/{location_place_id}/campaigns

        Params: location_place_id
        Response: LocationPlaceCampaignsResponse
        Auth: required
        """
        return self._client.call('get_location_places_location_place_id_campaigns',
            path={'location_place_id': location_place_id},
            headers=headers,
        )

    def get_location_places_location_place_id_media_items(self, location_place_id, *, page: Any = None, per: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET location_places/{location_place_id}/media_items

        Params: location_place_id, page, per
        Response: LocationPlaceMediaItemsResponse
        Auth: required
        """
        return self._client.call('get_location_places_location_place_id_media_items',
            path={'location_place_id': location_place_id},
            query={'page': page, 'per': per},
            headers=headers,
        )

    def get_location_places_nearby(self, *, latitude: Any = None, longitude: Any = None, radius_km: Any = None, page: Any = None, per: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET location_places/nearby

        Params: latitude, longitude, radius_km, page, per
        Response: LocationPlacesResponse
        Auth: required
        """
        return self._client.call('get_location_places_nearby',
            query={'latitude': latitude, 'longitude': longitude, 'radius_km': radius_km, 'page': page, 'per': per},
            headers=headers,
        )

    def get_location_places_search(self, *, query: Any = None, latitude: Any = None, longitude: Any = None, offset: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET location_places/search

        Params: query, latitude, longitude, offset
        Response: PlaceSearchResponse
        Auth: required
        """
        return self._client.call('get_location_places_search',
            query={'query': query, 'latitude': latitude, 'longitude': longitude, 'offset': offset},
            headers=headers,
        )

    def get_location_trigger_events(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET location/trigger_events
        Response: LocationTriggerEventsResponse
        Auth: required
        """
        return self._client.call('get_location_trigger_events',
            headers=headers,
        )

    def get_locations(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET locations
        Response: UserLocationsResponse
        Auth: required
        """
        return self._client.call('get_locations',
            headers=headers,
        )

    def get_maintenance(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET maintenance
        Response: ErrorsDTO
        Auth: required
        """
        return self._client.call('get_maintenance',
            headers=headers,
        )

    def get_memory_highlights_availability(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET memory_highlights/availability
        Response: MemoryHighlightsAvailabilityDTO
        Auth: required
        """
        return self._client.call('get_memory_highlights_availability',
            headers=headers,
        )

    def get_my(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET my
        Response: UserResponse
        Auth: required
        """
        return self._client.call('get_my',
            headers=headers,
        )

    def get_nearby_users_discoveries(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET nearby/users/discoveries
        Response: NearbyUsersDiscoveryResponse
        Auth: required
        """
        return self._client.call('get_nearby_users_discoveries',
            headers=headers,
        )

    def get_platform_locations_details_identifier(self, identifier, *, latitude: Any = None, longitude: Any = None, name: Any = None, address: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET platform_locations/details/{identifier}

        Params: identifier, latitude, longitude, name, address
        Response: PlatformLocationDetailsResponse
        Auth: required
        """
        return self._client.call('get_platform_locations_details_identifier',
            path={'identifier': identifier},
            query={'latitude': latitude, 'longitude': longitude, 'name': name, 'address': address},
            headers=headers,
        )

    def get_recommend_user_spots(self, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET recommend_user_spots

        Params: page
        Response: RecommendUserSpotsResponse
        Auth: required
        """
        return self._client.call('get_recommend_user_spots',
            query={'page': page},
            headers=headers,
        )

    def get_reverse_geocodes(self, *, latitude: Any = None, longitude: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET reverse_geocodes

        Params: latitude, longitude
        Response: ReverseGeocodesResponse
        Auth: required
        """
        return self._client.call('get_reverse_geocodes',
            query={'latitude': latitude, 'longitude': longitude},
            headers=headers,
        )

    def get_room_invite_link(self, *, code: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET room/invite_link

        Params: code
        Response: RoomInvitationResponse
        Auth: required
        """
        return self._client.call('get_room_invite_link',
            query={'code': code},
            headers=headers,
        )

    def get_rooms(self, *, limit: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms

        Params: limit
        Response: RoomsDTO
        Auth: required
        """
        return self._client.call('get_rooms',
            query={'limit': limit},
            headers=headers,
        )

    def get_rooms_2(self, *, limit: Any = None, name: Any = None, last_room_id: Any = None, include_all_states: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms

        Params: limit, name, last_room_id, include_all_states
        Response: RoomsDTO
        Auth: required
        """
        return self._client.call('get_rooms_2',
            query={'limit': limit, 'name': name, 'last_room_id': last_room_id, 'include_all_states': include_all_states},
            headers=headers,
        )

    def get_rooms_3(self, *, name: Any = None, last_room_id: Any = None, limit: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms

        Params: name, last_room_id, limit
        Response: RoomsDTO
        Auth: required
        """
        return self._client.call('get_rooms_3',
            query={'name': name, 'last_room_id': last_room_id, 'limit': limit},
            headers=headers,
        )

    def get_rooms_4(self, *, name: Any = None, limit: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms

        Params: name, limit
        Response: RoomsDTO
        Auth: required
        """
        return self._client.call('get_rooms_4',
            query={'name': name, 'limit': limit},
            headers=headers,
        )

    def get_rooms_5(self, *, last_room_id: Any = None, limit: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms

        Params: last_room_id, limit
        Response: RoomsDTO
        Auth: required
        """
        return self._client.call('get_rooms_5',
            query={'last_room_id': last_room_id, 'limit': limit},
            headers=headers,
        )

    def get_rooms_default_icon_images(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms/default_icon_images
        Response: DefaultIconImages
        Auth: required
        """
        return self._client.call('get_rooms_default_icon_images',
            headers=headers,
        )

    def get_rooms_id_invitation(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms/{id}/invitation

        Params: id
        Response: RoomInvitationDTO
        Auth: required
        """
        return self._client.call('get_rooms_id_invitation',
            path={'id': id},
            headers=headers,
        )

    def get_rooms_id_locations(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms/{id}/locations

        Params: id
        Response: UserLocationsResponse
        Auth: required
        """
        return self._client.call('get_rooms_id_locations',
            path={'id': id},
            headers=headers,
        )

    def get_rooms_id_messages(self, id, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms/{id}/messages

        Params: id, page
        Response: MessagesDTO
        Auth: required
        """
        return self._client.call('get_rooms_id_messages',
            path={'id': id},
            query={'page': page},
            headers=headers,
        )

    def get_rooms_id_users(self, id, *, page: Any = None, state: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms/{id}/users

        Params: id, page, state
        Response: RoomUsersResponse
        Auth: required
        """
        return self._client.call('get_rooms_id_users',
            path={'id': id},
            query={'page': page, 'state': state},
            headers=headers,
        )

    def get_rooms_room_id_presigned_url(self, room_id, *, filenames: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms/{room_id}/presigned_url

        Params: room_id, filenames[]
        Response: UploadMediaUrlDTO
        Auth: required
        """
        return self._client.call('get_rooms_room_id_presigned_url',
            path={'room_id': room_id},
            query={'filenames[]': filenames},
            headers=headers,
        )

    def get_rooms_room_id_streak(self, room_id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms/{room_id}/streak

        Params: room_id
        Response: RoomStreakResponse
        Auth: required
        """
        return self._client.call('get_rooms_room_id_streak',
            path={'room_id': room_id},
            headers=headers,
        )

    def get_rooms_streaks(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET rooms/streaks
        Response: RoomStreaksResponse
        Auth: required
        """
        return self._client.call('get_rooms_streaks',
            headers=headers,
        )

    def get_seasonal_challenges_challenge_code_status(self, challenge_code, *, is_in_japan: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET seasonal_challenges/{challenge_code}/status

        Params: challenge_code, is_in_japan
        Response: SeasonalChallengeStatusResponse
        Auth: required
        """
        return self._client.call('get_seasonal_challenges_challenge_code_status',
            path={'challenge_code': challenge_code},
            query={'is_in_japan': is_in_japan},
            headers=headers,
        )

    def get_seasonal_challenges_friends_icon_rings(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET seasonal_challenges/friends/icon_rings
        Response: FriendsIconRingsResponse
        Auth: required
        """
        return self._client.call('get_seasonal_challenges_friends_icon_rings',
            headers=headers,
        )

    def get_seasonal_challenges_icon_rings_me(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET seasonal_challenges/icon_rings/me
        Response: MyIconRingResponse
        Auth: required
        """
        return self._client.call('get_seasonal_challenges_icon_rings_me',
            headers=headers,
        )

    def get_sleep_time_friends(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET sleep_time/friends
        Response: SleepingFriendsResponse
        Auth: required
        """
        return self._client.call('get_sleep_time_friends',
            headers=headers,
        )

    def get_stamp_messages(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET stamp_messages
        Response: StampMessagesDTO
        Auth: required
        """
        return self._client.call('get_stamp_messages',
            headers=headers,
        )

    def get_stamp_sheet_products(self, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET stamp_sheet_products

        Params: page
        Response: StampSheetProductResponseDTO
        Auth: required
        """
        return self._client.call('get_stamp_sheet_products',
            query={'page': page},
            headers=headers,
        )

    def get_stamp_sheet_products_2(self, *, page: Any = None, type: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET stamp_sheet_products

        Params: page, type
        Response: StampSheetProductResponseDTO
        Auth: required
        """
        return self._client.call('get_stamp_sheet_products_2',
            query={'page': page, 'type': type},
            headers=headers,
        )

    def get_stamps_default_reaction_stamps(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET stamps/default_reaction_stamps
        Response: DefaultReactionListDTO
        Auth: required
        """
        return self._client.call('get_stamps_default_reaction_stamps',
            headers=headers,
        )

    def get_stamps_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET stamps/{id}

        Params: id
        Response: RandomStampResponse
        Auth: required
        """
        return self._client.call('get_stamps_id',
            path={'id': id},
            headers=headers,
        )

    def get_stamps_reaction_stamps(self, *, keywords: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET stamps/reaction_stamps

        Params: keywords
        Response: ReactionListDTO
        Auth: required
        """
        return self._client.call('get_stamps_reaction_stamps',
            query={'keywords': keywords},
            headers=headers,
        )

    def get_support_tickets(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET support/tickets
        Response: SupportTicketsResponse
        Auth: required
        """
        return self._client.call('get_support_tickets',
            headers=headers,
        )

    def get_support_tickets_id_messages(self, id, *, after_id: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET support/tickets/{id}/messages

        Params: id, after_id
        Response: SupportMessagesResponse
        Auth: required
        """
        return self._client.call('get_support_tickets_id_messages',
            path={'id': id},
            query={'after_id': after_id},
            headers=headers,
        )

    def get_thirdparty_services(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET thirdparty_services
        Response: ThirdPartyServicesIntegrationStatusResponse
        Auth: required
        """
        return self._client.call('get_thirdparty_services',
            headers=headers,
        )

    def get_user_app_versions(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/app_versions
        Response: UserAppVersionResponse
        Auth: required
        """
        return self._client.call('get_user_app_versions',
            headers=headers,
        )

    def get_user_blocks(self, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user_blocks

        Params: page
        Response: BlockUsersDTO
        Auth: required
        """
        return self._client.call('get_user_blocks',
            query={'page': page},
            headers=headers,
        )

    def get_user_boom_friend_locations_bump_summary_id(self, bump_summary_id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/boom_friend_locations/{bump_summary_id}

        Params: bump_summary_id
        Response: BoomFriendLocationsResponse
        Auth: required
        """
        return self._client.call('get_user_boom_friend_locations_bump_summary_id',
            path={'bump_summary_id': bump_summary_id},
            headers=headers,
        )

    def get_user_bump(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/bump
        Response: BumpResponse
        Auth: required
        """
        return self._client.call('get_user_bump',
            headers=headers,
        )

    def get_user_checkins_marked_checkins(self, *, user_id: Any = None, exclude_user_ids: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user_checkins/marked_checkins

        Params: user_id, exclude_user_ids
        Response: MarkedCheckInsResponse
        Auth: required
        """
        return self._client.call('get_user_checkins_marked_checkins',
            query={'user_id': user_id, 'exclude_user_ids': exclude_user_ids},
            headers=headers,
        )

    def get_user_checkins_marked_checkins_friends(self, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user_checkins/marked_checkins/friends

        Params: page
        Response: MarkedCheckInFriendsResponse
        Auth: required
        """
        return self._client.call('get_user_checkins_marked_checkins_friends',
            query={'page': page},
            headers=headers,
        )

    def get_user_music_now_playing(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/music/now_playing
        Response: NowPlayingMusicResponse
        Auth: required
        """
        return self._client.call('get_user_music_now_playing',
            headers=headers,
        )

    def get_user_music_recently_played(self, *, page: Any = None, user_id: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/music/recently_played

        Params: page, user_id
        Response: RecentlyPlayedMusicResponse
        Auth: required
        """
        return self._client.call('get_user_music_recently_played',
            query={'page': page, 'user_id': user_id},
            headers=headers,
        )

    def get_user_original_stamp_sheets(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/original_stamp_sheets
        Response: OriginalStampSheetDTO
        Auth: required
        """
        return self._client.call('get_user_original_stamp_sheets',
            headers=headers,
        )

    def get_user_original_stamps_presigned_url(self, *, cached_content_index_exi: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/original_stamps/presigned_url

        Params: cached_content_index.exi
        Response: UploadOriginalStampsUrlResponse
        Auth: required
        """
        return self._client.call('get_user_original_stamps_presigned_url',
            query={'cached_content_index.exi': cached_content_index_exi},
            headers=headers,
        )

    def get_user_profile_images_presigned_url(self, *, filename: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/profile_images/presigned_url

        Params: filename
        Response: UploadProfileImageUrlDTO
        Auth: required
        """
        return self._client.call('get_user_profile_images_presigned_url',
            query={'filename': filename},
            headers=headers,
        )

    def get_user_setting_banner(self, *, is_in_japan: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/setting_banner

        Params: is_in_japan
        Response: SettingBannerResponse
        Auth: required
        """
        return self._client.call('get_user_setting_banner',
            query={'is_in_japan': is_in_japan},
            headers=headers,
        )

    def get_user_spots(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET user/spots
        Response: UserSpotsDTO
        Auth: required
        """
        return self._client.call('get_user_spots',
            headers=headers,
        )

    def get_users_id_leaderboard(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET users/{id}/leaderboard

        Params: id
        Response: FriendsDTO
        Auth: required
        """
        return self._client.call('get_users_id_leaderboard',
            path={'id': id},
            headers=headers,
        )

    def get_users_id_pops(self, id, *, page: Any = None, per: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET users/{id}/pops

        Params: id, page, per
        Response: FriendsDTO
        Auth: required
        """
        return self._client.call('get_users_id_pops',
            path={'id': id},
            query={'page': page, 'per': per},
            headers=headers,
        )

    def get_users_id_room(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET users/{id}/room

        Params: id
        Response: MessagesDTO
        Auth: required
        """
        return self._client.call('get_users_id_room',
            path={'id': id},
            headers=headers,
        )

    def get_users_user_id_footprints(self, user_id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET users/{user_id}/footprints

        Params: user_id
        Response: FootprintUrlDTO
        Auth: required
        """
        return self._client.call('get_users_user_id_footprints',
            path={'user_id': user_id},
            headers=headers,
        )

    def get_users_user_name_username(self, user_name, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET users/{user_name}/username

        Params: user_name
        Response: UserDetailDTO
        Auth: required
        """
        return self._client.call('get_users_user_name_username',
            path={'user_name': user_name},
            headers=headers,
        )

    def get_v2_rooms_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/rooms/{id}

        Params: id
        Response: RoomResponse
        Auth: required
        """
        return self._client.call('get_v2_rooms_id',
            path={'id': id},
            headers=headers,
        )

    def get_v2_stamp_sheets(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/stamp_sheets
        Response: DefaultStampSheetsDTO
        Auth: required
        """
        return self._client.call('get_v2_stamp_sheets',
            headers=headers,
        )

    def get_v2_stamp_sheets_room_stamp_sheets(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/stamp_sheets/room_stamp_sheets
        Response: MessageStampListDTO
        Auth: required
        """
        return self._client.call('get_v2_stamp_sheets_room_stamp_sheets',
            headers=headers,
        )

    def get_v2_stamp_sheets_unlocked_stamp_sheets(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/stamp_sheets/unlocked_stamp_sheets
        Response: StampSheetsDTO
        Auth: required
        """
        return self._client.call('get_v2_stamp_sheets_unlocked_stamp_sheets',
            headers=headers,
        )

    def get_v2_user_checkins_id(self, id, *, from_: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/user_checkins/{id}

        Params: id, from
        Response: UserCheckInDetailResponse
        Auth: required
        """
        return self._client.call('get_v2_user_checkins_id',
            path={'id': id},
            query={'from': from_},
            headers=headers,
        )

    def get_v2_user_checkins_id_friend_checkin(self, id, *, friend_checkin_id: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/user_checkins/{id}/friend_checkin

        Params: id, friend_checkin_id
        Response: FriendCheckInResponse
        Auth: required
        """
        return self._client.call('get_v2_user_checkins_id_friend_checkin',
            path={'id': id},
            query={'friend_checkin_id': friend_checkin_id},
            headers=headers,
        )

    def get_v2_user_checkins_id_nearby_search_locations(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/user_checkins/{id}/nearby_search_locations

        Params: id
        Response: NearbySearchLocationsResponse
        Auth: required
        """
        return self._client.call('get_v2_user_checkins_id_nearby_search_locations',
            path={'id': id},
            headers=headers,
        )

    def get_v2_user_checkins_id_should_suggest_spot(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/user_checkins/{id}/should_suggest_spot

        Params: id
        Response: ShouldSuggestSpotResponse
        Auth: required
        """
        return self._client.call('get_v2_user_checkins_id_should_suggest_spot',
            path={'id': id},
            headers=headers,
        )

    def get_v2_user_checkins_platform_location_items_identifier(self, identifier, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/user_checkins/platform_location_items/{identifier}

        Params: identifier
        Response: PlatformLocationItemResponse
        Auth: required
        """
        return self._client.call('get_v2_user_checkins_platform_location_items_identifier',
            path={'identifier': identifier},
            headers=headers,
        )

    def get_v2_user_checkins_platform_location_items_identifier_friend_checkins(self, identifier, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/user_checkins/platform_location_items/{identifier}/friend_checkins

        Params: identifier, page
        Response: FriendCheckInsResponse
        Auth: required
        """
        return self._client.call('get_v2_user_checkins_platform_location_items_identifier_friend_checkins',
            path={'identifier': identifier},
            query={'page': page},
            headers=headers,
        )

    def get_v2_user_checkins_questions(self, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/user_checkins/questions

        Params: page
        Response: UserCheckInQuestionsResponse
        Auth: required
        """
        return self._client.call('get_v2_user_checkins_questions',
            query={'page': page},
            headers=headers,
        )

    def get_v2_user_checkins_spots(self, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/user_checkins/spots

        Params: page
        Response: UserCheckInSpotsResponse
        Auth: required
        """
        return self._client.call('get_v2_user_checkins_spots',
            query={'page': page},
            headers=headers,
        )

    def get_v2_users_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/users/{id}

        Params: id
        Response: UserDetailDTO
        Auth: required
        """
        return self._client.call('get_v2_users_id',
            path={'id': id},
            headers=headers,
        )

    def get_v2_users_id_2(self, id, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/users/{id}

        Params: id, page
        Response: FriendsDTO
        Auth: required
        """
        return self._client.call('get_v2_users_id_2',
            path={'id': id},
            query={'page': page},
            headers=headers,
        )

    def get_v2_watch_log_watch_count(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/watch_log/watch_count
        Response: WatchCountResponse
        Auth: required
        """
        return self._client.call('get_v2_watch_log_watch_count',
            headers=headers,
        )

    def get_v2_watch_log_watched_by(self, *, period: Any = None, page: Any = None, per: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/watch_log/watched_by

        Params: period, page, per
        Response: WatchLogResponse
        Auth: required
        """
        return self._client.call('get_v2_watch_log_watched_by',
            query={'period': period, 'page': page, 'per': per},
            headers=headers,
        )

    def get_v2_watch_log_watching(self, *, page: Any = None, per: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/watch_log/watching

        Params: page, per
        Response: WatchLogResponse
        Auth: required
        """
        return self._client.call('get_v2_watch_log_watching',
            query={'page': page, 'per': per},
            headers=headers,
        )

    def get_v2_whatsup_mixed_video_exists(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/whatsup/mixed_video/exists
        Response: WhatsUpMixedVideoExistsResponse
        Auth: required
        """
        return self._client.call('get_v2_whatsup_mixed_video_exists',
            headers=headers,
        )

    def get_v2_whatsup_original_mixed_video(self, *, slot_at: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/whatsup/original_mixed_video

        Params: slot_at
        Response: WhatsUpOriginalMixedVideoResponse
        Auth: required
        """
        return self._client.call('get_v2_whatsup_original_mixed_video',
            query={'slot_at': slot_at},
            headers=headers,
        )

    def get_v2_whatsup_video_current_slot_status(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/whatsup_video/current_slot_status
        Response: WhatsUpCurrentSlotStatusResponse
        Auth: required
        """
        return self._client.call('get_v2_whatsup_video_current_slot_status',
            headers=headers,
        )

    def get_v2_whatsup_video_id_reactions(self, id, *, page: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/whatsup_video/{id}/reactions

        Params: id, page
        Response: WhatsUpReactorsResponse
        Auth: required
        """
        return self._client.call('get_v2_whatsup_video_id_reactions',
            path={'id': id},
            query={'page': page},
            headers=headers,
        )

    def get_v2_whatsup_video_messages_message_id(self, message_id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/whatsup_video/messages/{message_id}

        Params: message_id
        Response: WhatsUpReplyMessageVideoResponse
        Auth: required
        """
        return self._client.call('get_v2_whatsup_video_messages_message_id',
            path={'message_id': message_id},
            headers=headers,
        )

    def get_v2_whatsup_video_presigned_url(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/whatsup_video/presigned_url
        Response: WhatsUpPresignedUrlResponse
        Auth: required
        """
        return self._client.call('get_v2_whatsup_video_presigned_url',
            headers=headers,
        )

    def get_v2_whatsup_video_reaction_stamps(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/whatsup_video/reaction_stamps
        Response: WhatsUpReactionStampsResponse
        Auth: required
        """
        return self._client.call('get_v2_whatsup_video_reaction_stamps',
            headers=headers,
        )

    def get_v2_whatsup_video_timeline(self, *, page: Any = None, per: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/whatsup_video/timeline

        Params: page, per
        Response: WhatsUpTimelineResponse
        Auth: required
        """
        return self._client.call('get_v2_whatsup_video_timeline',
            query={'page': page, 'per': per},
            headers=headers,
        )

    def get_v2_whatsup_video_users_user_id_status(self, user_id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET v2/whatsup_video/users/{user_id}/status

        Params: user_id
        Response: WhatsUpStatusResponse
        Auth: required
        """
        return self._client.call('get_v2_whatsup_video_users_user_id_status',
            path={'user_id': user_id},
            headers=headers,
        )

    def get_whoo_premium_memory_highlights_location_places(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET whoo_premium/memory_highlights/location_places
        Response: MemoryHighlightsLocationPlacesRankingResponseDTO
        Auth: required
        """
        return self._client.call('get_whoo_premium_memory_highlights_location_places',
            headers=headers,
        )

    def get_whoo_premium_memory_highlights_time_with_count_friends(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET whoo_premium/memory_highlights/time_with_count_friends
        Response: MemoryHighlightsFriendRankingResponseDTO
        Auth: required
        """
        return self._client.call('get_whoo_premium_memory_highlights_time_with_count_friends',
            headers=headers,
        )

    def get_whoo_premium_memory_highlights_time_with_users(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET whoo_premium/memory_highlights/time_with_users
        Response: MemoryHighlightsTimeWithUsersRankingResponseDTO
        Auth: required
        """
        return self._client.call('get_whoo_premium_memory_highlights_time_with_users',
            headers=headers,
        )

    def get_whoo_premium_memory_highlights_watched_by(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET whoo_premium/memory_highlights/watched_by
        Response: MemoryHighlightsFriendRankingResponseDTO
        Auth: required
        """
        return self._client.call('get_whoo_premium_memory_highlights_watched_by',
            headers=headers,
        )

    def get_whoo_premium_memory_highlights_watching(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET whoo_premium/memory_highlights/watching
        Response: MemoryHighlightsFriendRankingResponseDTO
        Auth: required
        """
        return self._client.call('get_whoo_premium_memory_highlights_watching',
            headers=headers,
        )

    def get_whoo_premium_messages_message_id_whatsup(self, messageId, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET whoo_premium/messages/{messageId}/whatsup

        Params: messageId
        Response: WhatsUp
        Auth: required
        """
        return self._client.call('get_whoo_premium_messages_message_id_whatsup',
            path={'messageId': messageId},
            headers=headers,
        )

    def get_whoo_premium_v2_premium_user(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """GET whoo_premium/v2/premium_user
        Response: PremiumUserResponse
        Auth: required
        """
        return self._client.call('get_whoo_premium_v2_premium_user',
            headers=headers,
        )

    def patch_email_user(self, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH email/user
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: AuthUserResponseDTO
        Auth: required
        """
        return self._client.call('patch_email_user',
            parts=parts,
            headers=headers,
        )

    def patch_friendships_id_hold(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH friendships/{id}/hold

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('patch_friendships_id_hold',
            path={'id': id},
            headers=headers,
        )

    def patch_media_message_watch_logs_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH media_message_watch_logs/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('patch_media_message_watch_logs_id',
            path={'id': id},
            headers=headers,
        )

    def patch_password_change(self, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH password/change
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: ErrorsDTO
        Auth: required
        """
        return self._client.call('patch_password_change',
            parts=parts,
            headers=headers,
        )

    def patch_rooms_id(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH rooms/{id}

        Params: id
        Body: RoomRequestBody
        Response: RoomResponse
        Auth: required
        """
        return self._client.call('patch_rooms_id',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def patch_rooms_id_2(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH rooms/{id}

        Params: id
        Body: UpdateRoomRequest
        Response: empty
        Auth: required
        """
        return self._client.call('patch_rooms_id_2',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def patch_rooms_id_hide(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH rooms/{id}/hide

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('patch_rooms_id_hide',
            path={'id': id},
            headers=headers,
        )

    def patch_thirdparty_services_status(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH thirdparty_services/status
        Body: DisconnectThirdPartyServicesIntegrationRequest
        Response: empty
        Auth: required
        """
        return self._client.call('patch_thirdparty_services_status',
            body=body,
            headers=headers,
        )

    def patch_user(self, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: UserResponse
        Auth: required
        """
        return self._client.call('patch_user',
            parts=parts,
            headers=headers,
        )

    def patch_user_app_versions(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user/app_versions
        Body: UserAppVersionRequest
        Response: empty
        Auth: required
        """
        return self._client.call('patch_user_app_versions',
            body=body,
            headers=headers,
        )

    def patch_user_checkins_marked_checkins_id(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user_checkins/marked_checkins/{id}

        Params: id
        Body: UpdateMarkedCheckInRequest
        Response: empty
        Auth: required
        """
        return self._client.call('patch_user_checkins_marked_checkins_id',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def patch_user_location(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user/location
        Body: UserLocationRequestDTO
        Response: UpdateUserLocationResponseDTO
        Auth: required
        """
        return self._client.call('patch_user_location',
            body=body,
            headers=headers,
        )

    def patch_user_music_recently_played(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user/music/recently_played
        Body: UpdateRecentlyPlayedMusicRequest
        Response: empty
        Auth: required
        """
        return self._client.call('patch_user_music_recently_played',
            body=body,
            headers=headers,
        )

    def patch_user_offline(self, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user/offline
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: empty
        Auth: required
        """
        return self._client.call('patch_user_offline',
            parts=parts,
            headers=headers,
        )

    def patch_user_offline_2(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user/offline
        Response: empty
        Auth: required
        """
        return self._client.call('patch_user_offline_2',
            headers=headers,
        )

    def patch_user_online(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user/online
        Response: empty
        Auth: required
        """
        return self._client.call('patch_user_online',
            headers=headers,
        )

    def patch_user_profile_images(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user/profile_images
        Body: ChangeProfileImageRequest
        Response: ProfileImageResponse
        Auth: required
        """
        return self._client.call('patch_user_profile_images',
            body=body,
            headers=headers,
        )

    def patch_user_spots_id(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH user/spots/{id}

        Params: id
        Body: UserSpotUpdateRequest
        Response: UserSpotResponse
        Auth: required
        """
        return self._client.call('patch_user_spots_id',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def patch_v2_user_checkins_id(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH v2/user_checkins/{id}

        Params: id
        Body: UpdateUserCheckInRequest
        Response: RegisteredSpotResponse
        Auth: required
        """
        return self._client.call('patch_v2_user_checkins_id',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def patch_v2_whatsup_video_id(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH v2/whatsup_video/{id}

        Params: id
        Body: UpdateWhatsUpCaptionRequest
        Response: empty
        Auth: required
        """
        return self._client.call('patch_v2_whatsup_video_id',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def patch_whoo_premium_premium_user_settings(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PATCH whoo_premium/premium_user_settings
        Body: PremiumUserSettingsRequest
        Response: empty
        Auth: required
        """
        return self._client.call('patch_whoo_premium_premium_user_settings',
            body=body,
            headers=headers,
        )

    def post_ab_test_content_id_watch(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST ab_test/content/{id}/watch

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('post_ab_test_content_id_watch',
            path={'id': id},
            headers=headers,
        )

    def post_activity_logs(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST activity_logs
        Body: ActivityLogRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_activity_logs',
            body=body,
            headers=headers,
        )

    def post_checkins_checkin_id_spots(self, checkin_id, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST checkins/{checkin_id}/spots

        Params: checkin_id
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: CheckInSpotResponse
        Auth: required
        """
        return self._client.call('post_checkins_checkin_id_spots',
            path={'checkin_id': checkin_id},
            parts=parts,
            headers=headers,
        )

    def post_directions_v2_compute_routes(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST directions/v2:computeRoutes
        Body: ComputeRoutesRequest
        Response: ComputeRoutesResponse
        Auth: not required
        """
        return self._client.call('post_directions_v2_compute_routes',
            body=body,
            headers=headers,
        )

    def post_email_login(self, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST email/login
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: UserResponse
        Auth: not required
        """
        return self._client.call('post_email_login',
            parts=parts,
            headers=headers,
        )

    def post_email_users(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST email/users
        Body: UserAccount
        Response: UserResponse
        Auth: not required
        """
        return self._client.call('post_email_users',
            body=body,
            headers=headers,
        )

    def post_footprint_download_status_failed(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST footprint/download_status/failed
        Response: empty
        Auth: required
        """
        return self._client.call('post_footprint_download_status_failed',
            headers=headers,
        )

    def post_footprint_download_status_success(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST footprint/download_status/success
        Response: empty
        Auth: required
        """
        return self._client.call('post_footprint_download_status_success',
            headers=headers,
        )

    def post_footprint_upload_complete(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST footprint/upload/complete
        Response: empty
        Auth: required
        """
        return self._client.call('post_footprint_upload_complete',
            headers=headers,
        )

    def post_friends(self, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST friends
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: FriendDTO
        Auth: required
        """
        return self._client.call('post_friends',
            parts=parts,
            headers=headers,
        )

    def post_friends_2(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST friends
        Body: FriendRequestDTO
        Response: FriendDetailDTO
        Auth: required
        """
        return self._client.call('post_friends_2',
            body=body,
            headers=headers,
        )

    def post_messages_message_id_message_reactions(self, messageId, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST messages/{messageId}/message_reactions

        Params: messageId
        Body: MessageReactionRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_messages_message_id_message_reactions',
            path={'messageId': messageId},
            body=body,
            headers=headers,
        )

    def post_nearby_users_discoveries(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST nearby/users/discoveries
        Body: NearbyUsersDiscoveryRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_nearby_users_discoveries',
            body=body,
            headers=headers,
        )

    def post_nearby_users_discoveries_user_id_friend_request(self, user_id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST nearby/users/discoveries/{user_id}/friend_request

        Params: user_id
        Body: NearbyFriendRequestDTO
        Response: empty
        Auth: required
        """
        return self._client.call('post_nearby_users_discoveries_user_id_friend_request',
            path={'user_id': user_id},
            body=body,
            headers=headers,
        )

    def post_nearby_users_discoveries_user_id_friend_request_reject(self, user_id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST nearby/users/discoveries/{user_id}/friend_request/reject

        Params: user_id
        Response: empty
        Auth: required
        """
        return self._client.call('post_nearby_users_discoveries_user_id_friend_request_reject',
            path={'user_id': user_id},
            headers=headers,
        )

    def post_password_forget(self, *, email: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST password/forget
        Response: ErrorsDTO
        Auth: not required
        """
        return self._client.call('post_password_forget',
            form={'email': email},
            headers=headers,
        )

    def post_recommend_user_spots_id_user_spots(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST recommend_user_spots/{id}/user_spots

        Params: id
        Body: RecommendUserSpotRequest
        Response: SuggestSpotUserSpotResponse
        Auth: required
        """
        return self._client.call('post_recommend_user_spots_id_user_spots',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def post_room_invite_link(self, *, room_id: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST room/invite_link

        Params: room_id
        Response: GroupChatInviteLinkResponse
        Auth: required
        """
        return self._client.call('post_room_invite_link',
            query={'room_id': room_id},
            headers=headers,
        )

    def post_room_invite_link_approve(self, *, code: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST room/invite_link/approve

        Params: code
        Response: empty
        Auth: required
        """
        return self._client.call('post_room_invite_link_approve',
            query={'code': code},
            headers=headers,
        )

    def post_rooms(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST rooms
        Body: RoomRequestBody
        Response: RoomResponse
        Auth: required
        """
        return self._client.call('post_rooms',
            body=body,
            headers=headers,
        )

    def post_rooms_id_messages(self, id, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST rooms/{id}/messages

        Params: id
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: PostMessageDTO
        Auth: required
        """
        return self._client.call('post_rooms_id_messages',
            path={'id': id},
            parts=parts,
            headers=headers,
        )

    def post_rooms_id_users_add(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST rooms/{id}/users/add

        Params: id
        Body: GroupChatUserRequestBody
        Response: empty
        Auth: required
        """
        return self._client.call('post_rooms_id_users_add',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def post_rooms_id_users_approve(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST rooms/{id}/users/approve

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('post_rooms_id_users_approve',
            path={'id': id},
            headers=headers,
        )

    def post_rooms_id_users_reject(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST rooms/{id}/users/reject

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('post_rooms_id_users_reject',
            path={'id': id},
            headers=headers,
        )

    def post_rooms_id_whatsups(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST rooms/{id}/whatsups

        Params: id
        Body: RoomWhatsupBody
        Response: RoomWhatsupResponse
        Auth: required
        """
        return self._client.call('post_rooms_id_whatsups',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def post_rooms_pinned_rooms(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST rooms/pinned_rooms
        Body: PinnedRoomRequestBody
        Response: RoomResponse
        Auth: required
        """
        return self._client.call('post_rooms_pinned_rooms',
            body=body,
            headers=headers,
        )

    def post_sleep_time(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST sleep_time
        Body: SleepWakeupRequestDTO
        Response: empty
        Auth: required
        """
        return self._client.call('post_sleep_time',
            body=body,
            headers=headers,
        )

    def post_stamp_messages(self, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST stamp_messages
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: empty
        Auth: required
        """
        return self._client.call('post_stamp_messages',
            parts=parts,
            headers=headers,
        )

    def post_support_tickets(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST support/tickets
        Body: CreateSupportTicketRequest
        Response: SupportTicketResponse
        Auth: required
        """
        return self._client.call('post_support_tickets',
            body=body,
            headers=headers,
        )

    def post_support_tickets_id_messages(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST support/tickets/{id}/messages

        Params: id
        Body: SendSupportMessageRequest
        Response: SupportMessageResponse
        Auth: required
        """
        return self._client.call('post_support_tickets_id_messages',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def post_support_tickets_id_presigned_urls(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST support/tickets/{id}/presigned_urls

        Params: id
        Body: SupportPresignedUrlsRequest
        Response: SupportPresignedUrlsResponse
        Auth: required
        """
        return self._client.call('post_support_tickets_id_presigned_urls',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def post_support_tickets_id_read(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST support/tickets/{id}/read

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('post_support_tickets_id_read',
            path={'id': id},
            headers=headers,
        )

    def post_support_tickets_id_resolve(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST support/tickets/{id}/resolve

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('post_support_tickets_id_resolve',
            path={'id': id},
            headers=headers,
        )

    def post_thirdparty_services_activate(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST thirdparty_services/activate
        Body: ActivateThirdPartyServicesRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_thirdparty_services_activate',
            body=body,
            headers=headers,
        )

    def post_thirdparty_services_apple_music_token(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST thirdparty_services/apple_music/token
        Body: AppleMusicTokenRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_thirdparty_services_apple_music_token',
            body=body,
            headers=headers,
        )

    def post_user_bump(self, *, parts: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST user/bump
        Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])
        Response: empty
        Auth: required
        """
        return self._client.call('post_user_bump',
            parts=parts,
            headers=headers,
        )

    def post_user_checkin_push_notification_deliveries_id_open(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST user_checkin_push_notification_deliveries/{id}/open

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('post_user_checkin_push_notification_deliveries_id_open',
            path={'id': id},
            headers=headers,
        )

    def post_user_checkins_id_suggest_spots_user_spots(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST user_checkins/{id}/suggest_spots/user_spots

        Params: id
        Body: SuggestSpotRequest
        Response: SuggestSpotUserSpotResponse
        Auth: required
        """
        return self._client.call('post_user_checkins_id_suggest_spots_user_spots',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def post_user_location_end_stay(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST user/location/end_stay
        Body: EndStayRequestDTO
        Response: empty
        Auth: required
        """
        return self._client.call('post_user_location_end_stay',
            body=body,
            headers=headers,
        )

    def post_user_music_recently_played_stop(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST user/music/recently_played/stop
        Response: empty
        Auth: required
        """
        return self._client.call('post_user_music_recently_played_stop',
            headers=headers,
        )

    def post_user_original_stamp_messages(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST user/original_stamp_messages
        Body: OriginalStampRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_user_original_stamp_messages',
            body=body,
            headers=headers,
        )

    def post_user_original_stamps(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST user/original_stamps
        Body: MediaUploadRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_user_original_stamps',
            body=body,
            headers=headers,
        )

    def post_username_suggest(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST username/suggest
        Body: SuggestUsernameRequest
        Response: SuggestUsernameResponse
        Auth: required
        """
        return self._client.call('post_username_suggest',
            body=body,
            headers=headers,
        )

    def post_users_id_block(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST users/{id}/block

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('post_users_id_block',
            path={'id': id},
            headers=headers,
        )

    def post_users_id_hidden(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST users/{id}/hidden

        Params: id
        Response: UserHiddenDTO
        Auth: required
        """
        return self._client.call('post_users_id_hidden',
            path={'id': id},
            headers=headers,
        )

    def post_v2_stamp_sheets_unlock(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST v2/stamp_sheets/unlock
        Body: UnlockStampSheetRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_v2_stamp_sheets_unlock',
            body=body,
            headers=headers,
        )

    def post_v2_user_checkins(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST v2/user_checkins
        Body: CreateUserCheckInRequest
        Response: RegisteredSpotResponse
        Auth: required
        """
        return self._client.call('post_v2_user_checkins',
            body=body,
            headers=headers,
        )

    def post_v2_user_checkins_checkin_users(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST v2/user_checkins/checkin_users
        Body: CheckinUsersRequest
        Response: CheckinUsersResponse
        Auth: required
        """
        return self._client.call('post_v2_user_checkins_checkin_users',
            body=body,
            headers=headers,
        )

    def post_v2_whatsup_mixed_video_request_backend(self, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST v2/whatsup/mixed_video/request_backend
        Response: empty
        Auth: required
        """
        return self._client.call('post_v2_whatsup_mixed_video_request_backend',
            headers=headers,
        )

    def post_v2_whatsup_request_post(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST v2/whatsup/request_post
        Body: WhatsUpRequestPostRequest
        Response: WhatsUpRequestPostResponse
        Auth: required
        """
        return self._client.call('post_v2_whatsup_request_post',
            body=body,
            headers=headers,
        )

    def post_v2_whatsup_rooms_room_id_request_posts(self, room_id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST v2/whatsup/rooms/{room_id}/request_posts

        Params: room_id
        Response: WhatsUpRequestPostResponse
        Auth: required
        """
        return self._client.call('post_v2_whatsup_rooms_room_id_request_posts',
            path={'room_id': room_id},
            headers=headers,
        )

    def post_v2_whatsup_video(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST v2/whatsup_video
        Body: CreateWhatsUpRequest
        Response: WhatsUpCreatedResponse
        Auth: required
        """
        return self._client.call('post_v2_whatsup_video',
            body=body,
            headers=headers,
        )

    def post_v2_whatsup_video_id_reaction(self, id, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST v2/whatsup_video/{id}/reaction

        Params: id
        Body: WhatsUpReactionRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_v2_whatsup_video_id_reaction',
            path={'id': id},
            body=body,
            headers=headers,
        )

    def post_validate_email(self, *, email: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST validate/email
        Response: ErrorsDTO
        Auth: not required
        """
        return self._client.call('post_validate_email',
            form={'email': email},
            headers=headers,
        )

    def post_validate_username(self, *, username: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST validate/username
        Response: ErrorsDTO
        Auth: not required
        """
        return self._client.call('post_validate_username',
            form={'username': username},
            headers=headers,
        )

    def post_wakeup_time(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST wakeup_time
        Body: SleepWakeupRequestDTO
        Response: empty
        Auth: required
        """
        return self._client.call('post_wakeup_time',
            body=body,
            headers=headers,
        )

    def post_whoo_premium_android_premium_users(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST whoo_premium/android/premium_users
        Body: PurchaseVerificationRequest
        Response: PremiumUserResponse
        Auth: required
        """
        return self._client.call('post_whoo_premium_android_premium_users',
            body=body,
            headers=headers,
        )

    def post_whoo_premium_v2_subscription_grace_period_watch(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """POST whoo_premium/v2/subscription_grace_period/watch
        Body: SubscriptionGracePeriodWatchRequest
        Response: empty
        Auth: required
        """
        return self._client.call('post_whoo_premium_v2_subscription_grace_period_watch',
            body=body,
            headers=headers,
        )

    def put_friend_location_sharing(self, *, body: Any = None, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PUT friend/location_sharing
        Body: UpdateLocationSharingRequest
        Response: FriendsLocationSharingsDTO
        Auth: required
        """
        return self._client.call('put_friend_location_sharing',
            body=body,
            headers=headers,
        )

    def put_user_app_icons_id(self, id, *, headers: Optional[Mapping[str, str]] = None) -> Any:
        """PUT user/app_icons/{id}

        Params: id
        Response: empty
        Auth: required
        """
        return self._client.call('put_user_app_icons_id',
            path={'id': id},
            headers=headers,
        )
