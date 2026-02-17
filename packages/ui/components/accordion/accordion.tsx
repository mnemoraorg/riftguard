"use client"

import * as React from "react"
import { Accordion as AccordionPrimitive } from "radix-ui"

export function Accordion({ ...props }: React.ComponentProps<typeof AccordionPrimitive.Root>) {
  return <AccordionPrimitive.Root data-slot="accordion" {...props} />
}
