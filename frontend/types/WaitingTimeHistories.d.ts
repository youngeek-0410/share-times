export type UUID = string
export type OrganizationType = "M" | "E" | "I" | "C" | "A" | "CLUB"

export type Organization = {
    uuid: UUID
    name: string
    description: string
    type: OrganizationType
}

export type WaitingTimeHistory = {
    uuid: UUID
    waiting_time: number
    created_at: string
    organization: Organization
}

export type WaitingTimeHistoryObject = {
    [key: string]: WaitingTimeHistory
}

export type WaitingTimeHistories = WaitingTimeHistory[]
